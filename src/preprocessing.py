from __future__ import annotations
import os
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


HIGH_MISSING_COLS = ["numbcars", "dwllsize", "HHstatin"]

REDUNDANT_COLS = [
    "adjrev",
    "adjmou",
    "adjqty",
]


def load_raw(data_dir: str | Path) -> pd.DataFrame:
    data_dir = Path(data_dir)
    client = pd.read_csv(data_dir / "Client.csv")
    record = pd.read_csv(data_dir / "Record.csv")

    df = record.merge(client, on="Customer_ID", how="inner")
    assert df.shape[0] == 100_000, f"Unexpected row count: {df.shape[0]}"
    return df


def prepare_raw_data(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    df = df.copy()

    df = df.drop(columns=["Customer_ID"], errors="ignore")
    df = df.drop(columns=HIGH_MISSING_COLS, errors="ignore")
    df = df.drop(columns=REDUNDANT_COLS, errors="ignore")

    df["eqpdays"] = df["eqpdays"].clip(lower=0)

    eps = 1e-6
    for col in ["income", "dwlltype", "lor", "adults", "hnd_webcap", "prizm_social_one", "avg6mou"]:
        if col in df.columns:
            df[f"{col}_missing"] = df[col].isnull().astype(int)

    df["eqpdays_per_month"] = df["eqpdays"] / (df["months"] + eps)
    df["rev_per_mou"] = df["rev_Mean"] / (df["mou_Mean"] + eps)
    df["custcare_flag"] = (df["custcare_Mean"] > 0).astype(int)
    df["overage_ratio"] = df["ovrmou_Mean"] / (df["mou_Mean"] + eps)
    df["change_mou_pct"] = df["change_mou"] / (df["mou_Mean"].abs() + eps)

    df["eqp_tenure_ratio"] = df["eqpdays"] / (df["months"] * 30.4375 + eps)
    df["overage_rev_ratio"] = df["ovrrev_Mean"] / (df["rev_Mean"] + eps)
    df["vce_overage_share"] = df["vceovr_Mean"] / (df["ovrrev_Mean"] + eps)
    df["call_completion_rate"] = df["complete_Mean"] / (df["attempt_Mean"] + eps)
    df["drop_rate"] = df["drop_blk_Mean"] / (df["attempt_Mean"] + eps)
    df["unanswered_rate"] = df["unan_vce_Mean"] / (df["plcd_vce_Mean"] + eps)
    df["custcare_rate"] = df["custcare_Mean"] / (df["plcd_vce_Mean"] + eps)
    df["peak_vce_ratio"] = df["peak_vce_Mean"] / (df["plcd_vce_Mean"] + eps)
    df["recent_mou_trend"] = df["avg3mou"] / (df["avg6mou"] + eps)
    df["recent_rev_trend"] = df["avg3rev"] / (df["avg6rev"] + eps)
    df["handset_fatigue_flag"] = (
        (df["eqpdays"] > 365) & (df["months"] >= 10) & (df["months"] <= 24)
    ).astype(int)
    df["service_friction_index"] = (
        (df["drop_vce_Mean"] > 3).astype(int)
        + (df["blck_vce_Mean"] > 2).astype(int)
        + (df["custcare_Mean"] > 0).astype(int)
    )

    df["mou_vs_avgmou"] = df["mou_Mean"] / (df["avgmou"] + eps)
    df["rev_vs_avgrev"] = df["rev_Mean"] / (df["avgrev"] + eps)
    df["mou_trend_3_vs_life"] = df["avg3mou"] / (df["avgmou"] + eps)
    df["rev_trend_3_vs_life"] = df["avg3rev"] / (df["avgrev"] + eps)
    df["mou_drop_recent"] = df["mou_Mean"] - df["avg3mou"]
    df["rev_drop_recent"] = df["rev_Mean"] - df["avg3rev"]
    df["totrev_per_month"] = df["totrev"] / (df["months"] + eps)
    df["totmou_per_call"] = df["totmou"] / (df["totcalls"] + eps)
    df["totcalls_per_month"] = df["totcalls"] / (df["months"] + eps)
    df["models_per_phone"] = df["models"] / (df["phones"] + eps)
    df["lines_inactive"] = (df["uniqsubs"] - df["actvsubs"]).clip(lower=0)
    df["active_sub_ratio"] = df["actvsubs"] / (df["uniqsubs"] + eps)
    df["eqp_past_2yr_flag"] = (df["eqpdays"] > 730).astype(int)
    df["eqp_past_1yr_flag"] = (df["eqpdays"] > 365).astype(int)
    df["total_failure_rate"] = (df["drop_vce_Mean"] + df["blck_vce_Mean"]) / (df["plcd_vce_Mean"] + eps)
    df["failed_call_count"] = df["attempt_Mean"] - df["complete_Mean"]
    df["ovr_pct_of_bill"] = df["ovrrev_Mean"] / (df["totmrc_Mean"] + df["ovrrev_Mean"] + eps)
    df["roam_rev_ratio"] = df["roam_Mean"] / (df["rev_Mean"] + eps)
    df["discretionary_spend"] = df["rev_Mean"] - df["totmrc_Mean"]
    df["historical_rate_per_min"] = df["totrev"] / (df["totmou"] + eps)
    df["eqp_tenure_interaction"] = (df["eqpdays"] / 30.4375) * df["months"]
    df["data_user_flag"] = ((df["comp_dat_Mean"] > 0) | (df["plcd_dat_Mean"] > 0)).astype(int)
    df["webcap_flag"] = (df["hnd_webcap"] == "WCMB").astype(int)
    df["refurb_flag"] = (df["refurb_new"] == "R").astype(int)
    df["asl_active"] = (df["asl_flag"] == "Y").astype(int)

    df_eda = df.copy()
    return df, df_eda


def fit_transform_train_val_test(
    X_train: pd.DataFrame,
    X_val: pd.DataFrame,
    X_test: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    X_tr = X_train.copy()
    X_va = X_val.copy()
    X_te = X_test.copy()

    train_med_drop = X_tr["drop_vce_Mean"].median()
    X_tr["high_drop_flag"] = (X_tr["drop_vce_Mean"] > train_med_drop).astype(int)
    X_va["high_drop_flag"] = (X_va["drop_vce_Mean"] > train_med_drop).astype(int)
    X_te["high_drop_flag"] = (X_te["drop_vce_Mean"] > train_med_drop).astype(int)

    num_cols = X_tr.select_dtypes(include=[np.number]).columns
    train_medians = X_tr[num_cols].median()
    X_tr[num_cols] = X_tr[num_cols].fillna(train_medians)
    X_va[num_cols] = X_va[num_cols].fillna(train_medians)
    X_te[num_cols] = X_te[num_cols].fillna(train_medians)

    cat_cols = list(X_tr.select_dtypes(include=["object", "str"]).columns)
    for col in cat_cols:
        X_tr[col] = X_tr[col].fillna("Unknown").astype(str)
        X_va[col] = X_va[col].fillna("Unknown").astype(str)
        X_te[col] = X_te[col].fillna("Unknown").astype(str)

        le = LabelEncoder()
        X_tr[col] = le.fit_transform(X_tr[col])

        mapping = dict(zip(le.classes_, le.transform(le.classes_)))
        X_va[col] = X_va[col].map(lambda s: mapping.get(s, -1))
        X_te[col] = X_te[col].map(lambda s: mapping.get(s, -1))

    return X_tr, X_va, X_te
