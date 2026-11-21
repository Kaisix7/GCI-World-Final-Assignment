import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
import lightgbm as lgb
import xgboost as xgb
import catboost as cb

from preprocessing import load_raw, prepare_raw_data
from features import select_features_train


def run_5fold_cv_on_train(data_dir: str = "data/raw"):
    print("Loading raw data...")
    df_raw = load_raw(data_dir)
    df_struct, _ = prepare_raw_data(df_raw)

    X = df_struct.drop("churn", axis=1)
    y = df_struct["churn"]

    X_dev, X_test, y_dev, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_dev, y_dev, test_size=0.125, random_state=42, stratify=y_dev
    )

    print(f"Dataset Partitions: Train={len(X_train):,}, Val={len(X_val):,}, Test={len(X_test):,}")

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    model_factories = {
        "Tuned LightGBM V3": lambda: lgb.LGBMClassifier(
            n_estimators=550, learning_rate=0.025, num_leaves=48, max_depth=7,
            subsample=0.80, colsample_bytree=0.75, min_child_samples=40,
            reg_alpha=1.0, reg_lambda=2.0, cat_smooth=15.0, cat_l2=10.0,
            random_state=42, verbose=-1, n_jobs=-1
        ),
        "Baseline LightGBM": lambda: lgb.LGBMClassifier(
            n_estimators=300, learning_rate=0.05, max_depth=6,
            random_state=42, verbose=-1, n_jobs=-1
        ),
        "Tuned XGBoost V3": lambda: xgb.XGBClassifier(
            n_estimators=450, learning_rate=0.03, max_depth=5,
            subsample=0.80, colsample_bytree=0.75, min_child_weight=4,
            reg_alpha=1.0, reg_lambda=2.0, tree_method="hist",
            eval_metric="logloss", random_state=42, verbosity=0, n_jobs=-1
        ),
        "CatBoost V3": lambda: cb.CatBoostClassifier(
            iterations=600, learning_rate=0.035, depth=6, l2_leaf_reg=4.0,
            eval_metric="AUC", random_seed=42, verbose=0, thread_count=-1
        ),
        "Scaled Logistic Regression": None,
    }

    fold_scores = {name: [] for name in model_factories}
    fold_scores["Tri-Blend Benchmark"] = []

    for fold, (train_idx, val_idx) in enumerate(skf.split(X_train, y_train), 1):
        print(f"\n--- Fold {fold} / 5 ---")
        X_f_tr = X_train.iloc[train_idx].copy()
        y_f_tr = y_train.iloc[train_idx].copy()
        X_f_va = X_train.iloc[val_idx].copy()
        y_f_va = y_train.iloc[val_idx].copy()

        med_drop = X_f_tr["drop_vce_Mean"].median()
        X_f_tr["high_drop_flag"] = (X_f_tr["drop_vce_Mean"] > med_drop).astype(int)
        X_f_va["high_drop_flag"] = (X_f_va["drop_vce_Mean"] > med_drop).astype(int)

        num_cols = X_f_tr.select_dtypes(include=[np.number]).columns
        fold_medians = X_f_tr[num_cols].median()
        X_f_tr[num_cols] = X_f_tr[num_cols].fillna(fold_medians)
        X_f_va[num_cols] = X_f_va[num_cols].fillna(fold_medians)

        cat_cols = list(X_f_tr.select_dtypes(include=["object", "str"]).columns)
        for col in cat_cols:
            X_f_tr[col] = X_f_tr[col].fillna("Unknown").astype(str)
            X_f_va[col] = X_f_va[col].fillna("Unknown").astype(str)
            le = LabelEncoder()
            X_f_tr[col] = le.fit_transform(X_f_tr[col])
            mapping = dict(zip(le.classes_, le.transform(le.classes_)))
            X_f_va[col] = X_f_va[col].map(lambda s: mapping.get(s, -1))

        to_drop = select_features_train(X_f_tr, y_f_tr, threshold=0.95)
        X_f_tr = X_f_tr.drop(columns=to_drop)
        X_f_va = X_f_va.drop(columns=to_drop)

        p_lgb = None
        p_xgb = None
        p_cb = None

        for name, factory in model_factories.items():
            if name == "Scaled Logistic Regression":
                scaler = StandardScaler()
                X_s_tr = scaler.fit_transform(X_f_tr)
                X_s_va = scaler.transform(X_f_va)
                lr = LogisticRegression(max_iter=1000, random_state=42, C=0.5, solver="lbfgs")
                lr.fit(X_s_tr, y_f_tr)
                p = lr.predict_proba(X_s_va)[:, 1]
            else:
                m = factory()
                if "LightGBM" in name:
                    X_tr_lgb = X_f_tr.copy()
                    X_va_lgb = X_f_va.copy()
                    for col in [c for c in cat_cols if c in X_tr_lgb.columns]:
                        X_tr_lgb[col] = X_tr_lgb[col].astype("category")
                        X_va_lgb[col] = X_va_lgb[col].astype("category")
                    m.fit(X_tr_lgb, y_f_tr)
                    p = m.predict_proba(X_va_lgb)[:, 1]
                    if name == "Tuned LightGBM V3":
                        p_lgb = p
                else:
                    m.fit(X_f_tr, y_f_tr)
                    p = m.predict_proba(X_f_va)[:, 1]
                    if name == "Tuned XGBoost V3":
                        p_xgb = p
                    elif name == "CatBoost V3":
                        p_cb = p

            auc = roc_auc_score(y_f_va, p)
            fold_scores[name].append(auc)
            print(f"  {name}: {auc:.5f}")

        if p_lgb is not None and p_xgb is not None and p_cb is not None:
            p_blend = 0.50 * p_lgb + 0.30 * p_cb + 0.20 * p_xgb
            auc_blend = roc_auc_score(y_f_va, p_blend)
            fold_scores["Tri-Blend Benchmark"].append(auc_blend)
            print(f"  Tri-Blend Benchmark: {auc_blend:.5f}")

    print("\n" + "="*70)
    print("=== 5-FOLD CV ON 70,000 TRAINING RECORDS (PREPROCESSING WITHIN FOLD) ===")
    print("="*70)
    t_crit = stats.t.ppf(0.975, df=4)
    summary_data = []
    for name, scores in fold_scores.items():
        mean_auc = np.mean(scores)
        std_auc = np.std(scores, ddof=1)
        se_auc = std_auc / np.sqrt(len(scores))
        ci_t = (mean_auc - t_crit * se_auc, mean_auc + t_crit * se_auc)
        summary_data.append({
            "Model": name,
            "Fold 1": round(scores[0], 5),
            "Fold 2": round(scores[1], 5),
            "Fold 3": round(scores[2], 5),
            "Fold 4": round(scores[3], 5),
            "Fold 5": round(scores[4], 5),
            "Mean AUC": round(mean_auc, 5),
            "Std Dev": round(std_auc, 5),
            "SE": round(se_auc, 5),
            "t-95% CI Lower": round(ci_t[0], 5),
            "t-95% CI Upper": round(ci_t[1], 5),
        })

    summary_df = pd.DataFrame(summary_data)
    print(summary_df.to_string(index=False))
    summary_df.to_csv("data/processed/cv_5fold_train_results.csv", index=False)
    print("\nSaved results to data/processed/cv_5fold_train_results.csv")
    return summary_df


if __name__ == "__main__":
    run_5fold_cv_on_train()
