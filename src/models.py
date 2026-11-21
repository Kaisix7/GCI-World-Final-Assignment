from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix,
)
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier


def get_candidate_models() -> dict:
    return {
        "Tuned LightGBM V3": LGBMClassifier(
            n_estimators=550,
            learning_rate=0.025,
            num_leaves=48,
            max_depth=7,
            subsample=0.80,
            colsample_bytree=0.75,
            min_child_samples=40,
            reg_alpha=1.0,
            reg_lambda=2.0,
            cat_smooth=15.0,
            cat_l2=10.0,
            random_state=42,
            verbose=-1,
            n_jobs=-1,
        ),
        "Baseline LightGBM": LGBMClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            random_state=42,
            verbose=-1,
            n_jobs=-1,
        ),
        "Tuned XGBoost V3": XGBClassifier(
            n_estimators=450,
            learning_rate=0.03,
            max_depth=5,
            subsample=0.80,
            colsample_bytree=0.75,
            min_child_weight=4,
            reg_alpha=1.0,
            reg_lambda=2.0,
            tree_method="hist",
            eval_metric="logloss",
            random_state=42,
            verbosity=0,
            n_jobs=-1,
        ),
        "CatBoost V3": CatBoostClassifier(
            iterations=600,
            learning_rate=0.035,
            depth=6,
            l2_leaf_reg=4.0,
            eval_metric="AUC",
            random_seed=42,
            verbose=0,
            thread_count=-1,
        ),
        "Scaled Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("classifier", LogisticRegression(
                max_iter=1000,
                random_state=42,
                solver="lbfgs",
                C=0.5,
            )),
        ]),
    }


def predict_tri_blend(p_lgb: np.ndarray, p_cb: np.ndarray, p_xgb: np.ndarray) -> np.ndarray:
    return 0.50 * p_lgb + 0.30 * p_cb + 0.20 * p_xgb


def evaluate_predictions(y_true: pd.Series | np.ndarray, y_proba: np.ndarray, threshold: float = 0.50) -> dict:
    y_pred = (y_proba >= threshold).astype(int)
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "auc": roc_auc_score(y_true, y_proba),
        "f1": f1_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "confusion_matrix": confusion_matrix(y_true, y_pred),
        "y_pred": y_pred,
        "y_proba": y_proba,
    }
