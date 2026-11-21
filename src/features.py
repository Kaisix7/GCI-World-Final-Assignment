from __future__ import annotations

import numpy as np
import pandas as pd


POTENTIAL_LEAKAGE = [
    "change_mou",
    "change_rev",
    "change_mou_pct",
]


def check_leakage(df: pd.DataFrame, target: str = "churn") -> pd.DataFrame:
    num = df.select_dtypes(include=[np.number]).drop(columns=[target], errors="ignore")
    corrs = num.corrwith(df[target]).abs().sort_values(ascending=False)
    result = corrs.reset_index()
    result.columns = ["feature", "abs_corr_with_target"]
    result["leakage_flag"] = result["feature"].isin(POTENTIAL_LEAKAGE)
    return result


def select_features_train(
    X_train: pd.DataFrame, y_train: pd.Series, threshold: float = 0.95
) -> list[str]:
    num_df = X_train.select_dtypes(include=[np.number])
    corr_matrix = num_df.corr().abs()
    target_corr = num_df.corrwith(y_train).abs()

    to_drop: set[str] = set()
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )

    for col in upper.columns:
        highly_corr = upper.index[upper[col] > threshold].tolist()
        for corr_col in highly_corr:
            if target_corr.get(col, 0) >= target_corr.get(corr_col, 0):
                to_drop.add(corr_col)
            else:
                to_drop.add(col)

    return sorted(list(to_drop))


ACTIONABLE_FEATURES = [
    "eqpdays",
    "eqpdays_per_month",
    "hnd_price",
    "refurb_new",
    "custcare_Mean",
    "custcare_flag",
    "drop_vce_Mean",
    "blck_vce_Mean",
    "high_drop_flag",
    "ovrmou_Mean",
    "ovrrev_Mean",
    "overage_ratio",
]
