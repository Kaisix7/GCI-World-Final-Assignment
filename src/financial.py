from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any
from pathlib import Path
import pandas as pd
import numpy as np


ARPU: float = 50.0
CONTRACT_HORIZON_MONTHS: int = 18
LTV_GROSS: float = ARPU * CONTRACT_HORIZON_MONTHS

COST_RED: float = 80.0
COST_AMBER: float = 15.0

SUCCESS_RED: float = 0.25
SUCCESS_AMBER: float = 0.15

DEFAULT_EBITDA_MARGIN: float = 0.50


@dataclass
class TierResult:
    tier: str
    population: int
    population_pct: float
    churners: float
    churn_rate: float
    intervention_cost_per_cust: float
    total_cost: float
    success_rate_assumption: float
    expected_retained: float
    displayed_retained: int
    gross_revenue_protected: float
    estimated_ebitda_contribution_50: float
    standalone_be_gross: float
    standalone_be_ebitda50: float
    standalone_be_abs_churn_red_gross: float
    standalone_be_abs_churn_red_ebitda50: float


@dataclass
class FinancialSummary:
    name: str
    calculation_mode: str
    sample_size: int
    scale_factor: float
    tiers: Dict[str, TierResult]
    total_customers: int
    total_cost: float
    expected_total_retained: float
    displayed_total_retained: int
    gross_revenue_protected: float
    net_revenue_protected: float
    gross_net_benefit: float
    gross_revenue_multiple: float
    gross_revenue_to_cost_ratio: float
    gross_revenue_multiple_x: float
    gross_roi: float
    net_revenue_roi: float
    estimated_ebitda_contribution_50: float
    net_ebitda_contribution_50: float
    ebitda_roi_50: float
    joint_be_multiplier_gross: float
    joint_be_multiplier_ebitda50: float
    break_even_ebitda_margin: float


def compute_financial_model(
    tier_counts: dict[str, int],
    tier_churners: dict[str, float],
    scale_factor: float = 1.0,
    name: str = "Test Set (n=20,000)",
    mode: str = "Retrospective",
) -> FinancialSummary:
    total_pop = sum(tier_counts.values())
    assert total_pop > 0, "Total population must be positive."

    tiers: Dict[str, TierResult] = {}
    total_cost = 0.0
    expected_total_retained = 0.0

    n_red = int(tier_counts["Red"] * scale_factor)
    ch_red = float(tier_churners["Red"] * scale_factor)
    cr_red = ch_red / n_red if n_red > 0 else 0.0
    cost_red_tot = n_red * COST_RED
    ret_red_exp = ch_red * SUCCESS_RED
    rev_red = ret_red_exp * LTV_GROSS
    ebitda_red_50 = rev_red * DEFAULT_EBITDA_MARGIN
    be_red_gross = COST_RED / (cr_red * LTV_GROSS) if (cr_red * LTV_GROSS) > 0 else 1.0
    be_red_e50 = COST_RED / (cr_red * (LTV_GROSS * 0.5)) if (cr_red * LTV_GROSS) > 0 else 1.0
    be_red_abs_gross = COST_RED / LTV_GROSS
    be_red_abs_e50 = COST_RED / (LTV_GROSS * 0.5)

    tiers["Red"] = TierResult(
        tier="Red",
        population=n_red,
        population_pct=(n_red / (total_pop * scale_factor)) * 100,
        churners=ch_red,
        churn_rate=cr_red * 100,
        intervention_cost_per_cust=COST_RED,
        total_cost=cost_red_tot,
        success_rate_assumption=SUCCESS_RED * 100,
        expected_retained=ret_red_exp,
        displayed_retained=int(round(ret_red_exp)),
        gross_revenue_protected=rev_red,
        estimated_ebitda_contribution_50=ebitda_red_50,
        standalone_be_gross=be_red_gross * 100,
        standalone_be_ebitda50=be_red_e50 * 100,
        standalone_be_abs_churn_red_gross=be_red_abs_gross * 100,
        standalone_be_abs_churn_red_ebitda50=be_red_abs_e50 * 100,
    )
    total_cost += cost_red_tot
    expected_total_retained += ret_red_exp

    n_amb = int(tier_counts["Amber"] * scale_factor)
    ch_amb = float(tier_churners["Amber"] * scale_factor)
    cr_amb = ch_amb / n_amb if n_amb > 0 else 0.0
    cost_amb_tot = n_amb * COST_AMBER
    ret_amb_exp = ch_amb * SUCCESS_AMBER
    rev_amb = ret_amb_exp * LTV_GROSS
    ebitda_amb_50 = rev_amb * DEFAULT_EBITDA_MARGIN
    be_amb_gross = COST_AMBER / (cr_amb * LTV_GROSS) if (cr_amb * LTV_GROSS) > 0 else 1.0
    be_amb_e50 = COST_AMBER / (cr_amb * (LTV_GROSS * 0.5)) if (cr_amb * LTV_GROSS) > 0 else 1.0
    be_amb_abs_gross = COST_AMBER / LTV_GROSS
    be_amb_abs_e50 = COST_AMBER / (LTV_GROSS * 0.5)

    tiers["Amber"] = TierResult(
        tier="Amber",
        population=n_amb,
        population_pct=(n_amb / (total_pop * scale_factor)) * 100,
        churners=ch_amb,
        churn_rate=cr_amb * 100,
        intervention_cost_per_cust=COST_AMBER,
        total_cost=cost_amb_tot,
        success_rate_assumption=SUCCESS_AMBER * 100,
        expected_retained=ret_amb_exp,
        displayed_retained=int(round(ret_amb_exp)),
        gross_revenue_protected=rev_amb,
        estimated_ebitda_contribution_50=ebitda_amb_50,
        standalone_be_gross=be_amb_gross * 100,
        standalone_be_ebitda50=be_amb_e50 * 100,
        standalone_be_abs_churn_red_gross=be_amb_abs_gross * 100,
        standalone_be_abs_churn_red_ebitda50=be_amb_abs_e50 * 100,
    )
    total_cost += cost_amb_tot
    expected_total_retained += ret_amb_exp

    n_grn = int(tier_counts["Green"] * scale_factor)
    ch_grn = float(tier_churners["Green"] * scale_factor)
    cr_grn = ch_grn / n_grn if n_grn > 0 else 0.0

    tiers["Green"] = TierResult(
        tier="Green",
        population=n_grn,
        population_pct=(n_grn / (total_pop * scale_factor)) * 100,
        churners=ch_grn,
        churn_rate=cr_grn * 100,
        intervention_cost_per_cust=0.0,
        total_cost=0.0,
        success_rate_assumption=0.0,
        expected_retained=0.0,
        displayed_retained=0,
        gross_revenue_protected=0.0,
        estimated_ebitda_contribution_50=0.0,
        standalone_be_gross=0.0,
        standalone_be_ebitda50=0.0,
        standalone_be_abs_churn_red_gross=0.0,
        standalone_be_abs_churn_red_ebitda50=0.0,
    )

    gross_rev_protected = expected_total_retained * LTV_GROSS
    net_rev_protected = gross_rev_protected - total_cost
    gross_net_benefit = net_rev_protected
    gross_rev_to_cost_ratio = (gross_rev_protected / total_cost) * 100 if total_cost > 0 else 0.0
    gross_rev_mult_x = (gross_rev_protected / total_cost) if total_cost > 0 else 0.0
    gross_rev_mult = gross_rev_to_cost_ratio
    net_rev_roi = (net_rev_protected / total_cost) * 100 if total_cost > 0 else 0.0
    gross_roi = net_rev_roi

    ebitda_contrib_50 = gross_rev_protected * DEFAULT_EBITDA_MARGIN
    net_ebitda_50 = ebitda_contrib_50 - total_cost
    ebitda_roi_50 = (net_ebitda_50 / total_cost) * 100 if total_cost > 0 else 0.0

    joint_be_mult_gross = (total_cost / gross_rev_protected) if gross_rev_protected > 0 else 1.0
    joint_be_mult_e50 = (total_cost / ebitda_contrib_50) if ebitda_contrib_50 > 0 else 1.0
    be_margin = (total_cost / gross_rev_protected) * 100 if gross_rev_protected > 0 else 100.0

    return FinancialSummary(
        name=name,
        calculation_mode=mode,
        sample_size=int(total_pop * scale_factor),
        scale_factor=scale_factor,
        tiers=tiers,
        total_customers=int(total_pop * scale_factor),
        total_cost=total_cost,
        expected_total_retained=expected_total_retained,
        displayed_total_retained=int(round(expected_total_retained)),
        gross_revenue_protected=gross_rev_protected,
        net_revenue_protected=net_rev_protected,
        gross_net_benefit=gross_net_benefit,
        gross_revenue_multiple=gross_rev_mult,
        gross_revenue_to_cost_ratio=gross_rev_to_cost_ratio,
        gross_revenue_multiple_x=gross_rev_mult_x,
        gross_roi=gross_roi,
        net_revenue_roi=net_rev_roi,
        estimated_ebitda_contribution_50=ebitda_contrib_50,
        net_ebitda_contribution_50=net_ebitda_50,
        ebitda_roi_50=ebitda_roi_50,
        joint_be_multiplier_gross=joint_be_mult_gross * 100,
        joint_be_multiplier_ebitda50=joint_be_mult_e50 * 100,
        break_even_ebitda_margin=be_margin,
    )


def run_canonical_financial_analysis() -> tuple[FinancialSummary, FinancialSummary, FinancialSummary, FinancialSummary]:
    tier_counts = {"Red": 2351, "Amber": 7734, "Green": 9915}
    actual_churners = {"Red": 1848.0, "Amber": 4588.0, "Green": 3476.0}
    expected_churners = {"Red": 1840.35, "Amber": 4563.29, "Green": 3529.40}

    retro_a = compute_financial_model(
        tier_counts, actual_churners, scale_factor=1.0,
        name="Table A (Retrospective): Test Set (n=20,000)", mode="Retrospective"
    )
    retro_b = compute_financial_model(
        tier_counts, actual_churners, scale_factor=5.0,
        name="Table B (Retrospective): Enterprise Fleet (n=100,000)", mode="Retrospective"
    )

    prosp_a = compute_financial_model(
        tier_counts, expected_churners, scale_factor=1.0,
        name="Table A (Prospective): Test Set (n=20,000)", mode="Prospective"
    )
    prosp_b = compute_financial_model(
        tier_counts, expected_churners, scale_factor=5.0,
        name="Table B (Prospective): Enterprise Fleet (n=100,000)", mode="Prospective"
    )

    return retro_a, retro_b, prosp_a, prosp_b


def run_baseline_financial_analysis() -> tuple[FinancialSummary, FinancialSummary]:
    tier_counts = {"Red": 2094, "Amber": 7940, "Green": 9966}
    tier_churners = {"Red": 1656.0, "Amber": 4701.0, "Green": 3555.0}

    table_a = compute_financial_model(
        tier_counts, tier_churners, scale_factor=1.0,
        name="Table A (Baseline): Test Set (n=20,000)", mode="Retrospective"
    )
    table_b = compute_financial_model(
        tier_counts, tier_churners, scale_factor=5.0,
        name="Table B (Baseline): Enterprise Fleet (n=100,000)", mode="Retrospective"
    )
    return table_a, table_b


def export_financial_summary_csv(output_path: str = "data/processed/financial_summary.csv"):
    retro_a, retro_b, prosp_a, prosp_b = run_canonical_financial_analysis()
    records = []

    for summary in [retro_a, retro_b, prosp_a, prosp_b]:
        prefix = summary.name
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Tier Subscribers", "Value": summary.tiers["Red"].population, "Unit": "customers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Tier Churners", "Value": round(summary.tiers["Red"].churners, 2), "Unit": "churners"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Tier Retained (Expected)", "Value": round(summary.tiers["Red"].expected_retained, 2), "Unit": "subscribers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Tier Subscribers", "Value": summary.tiers["Amber"].population, "Unit": "customers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Tier Churners", "Value": round(summary.tiers["Amber"].churners, 2), "Unit": "churners"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Tier Retained (Expected)", "Value": round(summary.tiers["Amber"].expected_retained, 2), "Unit": "subscribers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Total Subscribers Protected (Expected)", "Value": round(summary.expected_total_retained, 2), "Unit": "subscribers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Total Subscribers Protected (Displayed)", "Value": summary.displayed_total_retained, "Unit": "subscribers"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Gross Revenue Protected", "Value": round(summary.gross_revenue_protected, 2), "Unit": "USD"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Campaign Cost", "Value": round(summary.total_cost, 2), "Unit": "USD"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Net Protected Revenue", "Value": round(summary.net_revenue_protected, 2), "Unit": "USD"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Net Revenue ROI", "Value": round(summary.net_revenue_roi, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Gross Revenue-to-Cost Ratio", "Value": round(summary.gross_revenue_to_cost_ratio, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Estimated EBITDA Contribution (50% margin)", "Value": round(summary.estimated_ebitda_contribution_50, 2), "Unit": "USD"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Net EBITDA Contribution (50% margin)", "Value": round(summary.net_ebitda_contribution_50, 2), "Unit": "USD"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "EBITDA-Based ROI (50% margin)", "Value": round(summary.ebitda_roi_50, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Standalone Break-Even (Gross)", "Value": round(summary.tiers["Red"].standalone_be_gross, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Standalone Break-Even (Gross)", "Value": round(summary.tiers["Amber"].standalone_be_gross, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Standalone Break-Even (50% EBITDA Margin)", "Value": round(summary.tiers["Red"].standalone_be_ebitda50, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Standalone Break-Even (50% EBITDA Margin)", "Value": round(summary.tiers["Amber"].standalone_be_ebitda50, 2), "Unit": "percent"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Red Break-Even Absolute Churn Reduction", "Value": round(summary.tiers["Red"].standalone_be_abs_churn_red_ebitda50, 2), "Unit": "percentage points"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Amber Break-Even Absolute Churn Reduction", "Value": round(summary.tiers["Amber"].standalone_be_abs_churn_red_ebitda50, 2), "Unit": "percentage points"})
        records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Joint Break-Even Multiplier (Gross)", "Value": round(summary.joint_be_multiplier_gross, 2), "Unit": "percent"})
        if "Enterprise" in prefix:
            records.append({"Scope": prefix, "Mode": summary.calculation_mode, "Dimension": "Break-Even EBITDA Margin", "Value": round(summary.break_even_ebitda_margin, 2), "Unit": "percent"})

    df = pd.DataFrame(records)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Exported financial summary to {output_path}")


if __name__ == "__main__":
    export_financial_summary_csv()
    r_a, r_b, p_a, p_b = run_canonical_financial_analysis()
    print("Retrospective Fleet Net Rev ROI:", f"{r_b.net_revenue_roi:.2f}%")
    print("Prospective Fleet Net Rev ROI:", f"{p_b.net_revenue_roi:.2f}%")
    print("Retrospective Fleet EBITDA ROI:", f"{r_b.ebitda_roi_50:.2f}%")
    print("Prospective Fleet EBITDA ROI:", f"{p_b.ebitda_roi_50:.2f}%")
