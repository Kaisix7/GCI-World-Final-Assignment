# Company A Telecom — Churn Prediction & Targeted Retention Strategy

## GCI World 2026 September Final Assignment

> **Author:** Karina B.  
> **Date:** November 2026  
> **Programme:** GCI World 2026 September  
> **Course Scenario:** Associate Consultant Proof of Concept (PoC) Business Model Proposal  

---

## 🗂️ Executive Overview

This repository contains an end-to-end, scientifically validated, reproducible Data Science portfolio project for **Company A**, an anonymous US wireless telecommunications operator with 100,000 subscriber records.

**Core Business Problem:**  
*"Which subscribers are most likely to churn, what actionable levers drive their disengagement, and what targeted retention programme yields the highest return on investment (ROI)?"*

### Audited Key Results

| Metric / Operational Dimension | Empirical Model Value | Methodological Derivation / Significance |
|:---|:---:|:---|
| **Champion Model** | **Tuned LightGBM V3** | Leaf-wise GBDT (550 trees, lr=0.025, leaves=48, max_depth=7); single dependency, native TreeSHAP |
| **Research Benchmark** | **Tri-Blend Ensemble** | 50% LightGBM V3 + 30% CatBoost V3 + 20% XGBoost V3; demonstrates predictive upper bound |
| **Paired Test Comparison Status** | **+0.0004 Observed Delta** | Single LightGBM V3 (0.7015) vs Tri-Blend (0.7019); test predictions not serialized; formal significance unverified from static files |
| **Leak-Free 5-Fold CV (70k Training Set)**| **0.70106 ± 0.00556** | Descriptive Student's t 95% interval: `[0.69416, 0.70796]` (df=4; fold-level variation per Bengio & Grandvalet, 2004) |
| **Tri-Blend 5-Fold CV (70k Training Set)**| **0.70263 ± 0.00566** | Descriptive Student's t 95% interval: `[0.69560, 0.70966]` |
| **Validation Set AUC-ROC** | **0.7051** (0.7052) | Evaluated across 10,000 validation holdout subscribers |
| **Reserved Test Set AUC-ROC** | **0.7015** | Evaluated on 20,000 reserved test subscribers with historical exploratory inspection |
| **Baseline Test Set AUC-ROC** | **0.6968** | Initial walkthrough baseline; Champion LightGBM V3 beats baseline by **+0.0047** |
| **Test Set Accuracy** | **64.38%** | +13.94 percentage points above naive 50.44% stayer baseline |
| **Test Set Recall (Sensitivity)** | **64.93%** | Captures nearly 2 out of every 3 impending churners |
| **Test Set Precision** | **63.82%** | High precision minimizing false-alarm intervention waste |
| **Primary Actionable Signal** | **Equipment Age (`eqpdays`)** | Churners hold devices **58 days older** on average (421 vs 363 days) |
| **Subscribers Protected (Fleet)** | **5,751.00 exp.** (5,751 displayed) | 2,310.00 (Red Tier) + 3,441.00 (Amber Tier) expected retained [+155 vs baseline] |
| **Primary Economic Metric: Net EBITDA Contribution**| **$1,067,500.00** | Under assumed 50% EBITDA margin scenario ($2,587,950 gross contrib − $1,520,450 cost) |
| **Primary Economic Metric: EBITDA-Based ROI**| **70.21%** | **Primary Management Decision Metric** (telecom industry-standard EBITDA benchmark) |
| **Gross Contractual Revenue Protected**| **$5,175,900.00** | $5,751.00 \times \$900$ LTV ($50/mo ARPU over 18-month contract) [+$139.7k vs baseline] |
| **Total Campaign Investment Cost** | **$1,520,450.00** | $(11,755 \times \$80) + (38,670 \times \$15)$ intervention investment |
| **Net Protected Revenue** | **$3,655,450.00** | Gross revenue protected minus campaign cost ($5,175,900 − $1,520,450) [+$52.4k vs baseline] |
| **Net Revenue ROI** | **240.42%** | $(\text{Net Protected Revenue} / \text{Campaign Cost}) \times 100$; gross multiple is **340.42% (3.40x)** |
| **Break-Even EBITDA Margin** | **29.38% EBITDA** | Minimum operating margin required for net positive EBITDA contribution |
| **Standalone Break-Even (50% EBITDA Margin)**| **Red: 22.62% \| Amber: 5.62%** | Standalone conditional response rate where segment net EBITDA contribution equals $0 |
| **Break-Even Absolute Churn Reduction**| **Red: 17.78 pp \| Amber: 3.33 pp**| Absolute percentage point churn-rate reduction required in randomized A/B test |
| **Joint Scaling Break-Even Multiplier** | **29.38% of baseline** | Proportional drop threshold: Red to **7.34%**, Amber to **4.41%** |
| **Reconciled Baseline Segmentation** | **5,595.75 retained** | Baseline model: $3.60M net revenue, 251.42% Net Rev ROI, 351.42% Gross Ratio, $1.08M net EBITDA |

---

## 📁 Repository Structure

```
GCI-World-Final-Assignment/
├── data/
│   ├── raw/                       ← Original CSVs (never modified or committed)
│   │   ├── Client.csv             ← 100,000 subscribers × 50 account/device features
│   │   └── Record.csv             ← 100,000 subscribers × 51 usage/billing metrics + churn
│   └── processed/                 ← Cleaned, leak-free intermediate model outputs
│       ├── cv_5fold_train_results.csv ← Audited 5-fold CV results table across models
│       ├── model_comparison.csv    ← Audited metrics across all candidate algorithms
│       ├── feature_importance.csv  ← Feature importance rankings and gain metrics
│       ├── financial_summary.csv   ← Canonical financial metrics (Table A & Table B)
│       ├── features_clean.csv      ← Cleaned feature set
│       └── oof_predictions_v3.csv  ← 70,000 out-of-fold predictions for V3 models
│
├── notebooks/
│   ├── analysis.ipynb             ← PRIMARY DELIVERABLE: Full reproducible analysis notebook (30 executed cells)
│   └── analysis_executed.ipynb    ← Verified clean-kernel executed notebook with all saved figures
│
├── src/                           ← Clean, modular Python source code (zero comments)
│   ├── preprocessing.py           ← Strictly leak-free data loading and train/val/test transformation
│   ├── features.py                ← Domain feature engineering and train-only collinearity filtering
│   ├── models.py                  ← Model definitions, hyperparameter configurations, and evaluation
│   ├── cross_validation.py        ← Leak-free 5-fold cross-validation on 70k training records
│   ├── financial.py               ← Canonical financial calculation module (unrounded expected values)
│   └── generate_presentation.py   ← Automated executive slide deck renderer (FPDF2, 15 slides)
│
├── reports/
│   ├── presentation.pdf           ← 15-SLIDE EXECUTIVE PRESENTATION (PDF format, 892 KB, exactly 15 slides)
│   └── references.md              ← Comprehensive reference list matching slide citations
│
├── images/                        ← 12 high-resolution, purpose-built visualizations
│   ├── 01_churn_distribution.png
│   ├── 02_eqpdays_vs_churn.png
│   ├── 03_revenue_usage_vs_churn.png
│   ├── 04_missing_values.png
│   ├── 05_model_comparison.png
│   ├── 06_roc_curves.png
│   ├── 07_confusion_matrix.png
│   ├── 08_feature_importance.png
│   ├── 09_shap_summary.png
│   ├── 10_churn_by_area.png
│   ├── 11_churn_by_tenure.png
│   └── 12_risk_score_distribution.png
│
├── drive-download-20261120T051651Z-1-001/  ← Original unzipped assignment package (preserved intact)
│   ├── Final Assignment/
│   │   ├── telecom/               ← Client.csv and Record.csv
│   │   ├── tutorial.ipynb         ← Official walkthrough notebook
│   │   ├── README.docx            ← Official requirements specification
│   │   └── ENG_Company_A_Dataset_Overview.docx
│   └── Sample Slides from Past Outstanding Students/
│
├── requirements.txt               ← Exact pinned dependencies for 100% reproducibility
├── .gitignore                     ← Excludes large binary CSVs and temporary caches
└── README.md                      ← Comprehensive project documentation
```

---

## 🔬 Methodology & Scientific Validation

### 1. Zero Data Leakage Architecture & Test Set Integrity
* **Structural Cleaning:** Unconditionally dropped customer identifier (`Customer_ID`), heavily missing columns with >35% missingness (`numbcars`, `dwllsize`, `HHstatin`), and collinear duplicates (`adjrev`, `adjmou`, `adjqty`).
* **Strict 3-Way Partition:** Data was split into:
  - **Training Set (70% = 70,000 subscribers):** Used exclusively to fit model parameters, learn numeric medians, and extract category frequency encodings.
  - **Validation Set (10% = 10,000 subscribers):** Used strictly for hyperparameter tuning, model selection, and risk score threshold calibration ($p_{\text{Amber}} = 0.50$, $p_{\text{Red}} = 0.70$).
  - **Reserved Test Partition (20% = 20,000 subscribers):** Reserved test partition with historical exploratory inspection; all models and thresholds locked prior to final test reporting.
* **Test Set Integrity Disclosure:** The test partition is a **reserved test partition with historical exploratory inspection**. Test-set metrics were inspected during early exploratory development, but the test set was **never** used for model selection, hyperparameter tuning, feature selection, or threshold calibration. All architectural decisions, hyperparameters, and threshold cutoffs were locked using training and validation data prior to final test partition scoring.
* **Train-Only Imputation & Encoding:** Medians for numeric features and category label encodings were calculated strictly on `X_train` and then applied to `X_val` and `X_test`. Unseen test categories are safely mapped to `-1`.
* **Train-Only Collinearity Filtering:** Features with pairwise correlation $>0.95$ were filtered based strictly on `X_train` variance and target correlation.

### 2. Rigorous Cross-Validation & Algorithmic Limits

To evaluate out-of-fold generalization without hyperparameter contamination, we performed a **leak-free 5-fold Stratified Cross-Validation strictly on the 70,000 training records** (`X_train`), where all numeric imputations, categorical frequency encodings, and multicollinearity filtering were fit independently inside each training fold (Train = 56,000, Val = 14,000):

| Model Architecture | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean AUC | Std Dev | SE | Descriptive Student's t 95% Interval (df=4)* |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Tri-Blend Benchmark (50/30/20)** | 0.7077 | 0.7076 | 0.7041 | 0.6946 | 0.6992 | **0.70263** | ±0.00566 | 0.00253 | `[0.69560, 0.70966]` |
| **Tuned LightGBM V3 (Champion)** | 0.7050 | 0.7070 | 0.7016 | 0.6928 | 0.6989 | **0.70106** | ±0.00556 | 0.00248 | `[0.69416, 0.70796]` |
| **Tuned XGBoost V3** | 0.7050 | 0.7035 | 0.7016 | 0.6924 | 0.6959 | **0.69967** | ±0.00531 | 0.00238 | `[0.69307, 0.70626]` |
| **CatBoost V3** | 0.7044 | 0.7020 | 0.7015 | 0.6914 | 0.6929 | **0.69844** | ±0.00589 | 0.00263 | `[0.69113, 0.70575]` |
| **Baseline LightGBM** | 0.7012 | 0.6981 | 0.6980 | 0.6883 | 0.6923 | **0.69559** | ±0.00516 | 0.00231 | `[0.68918, 0.70200]` |
| **Scaled Logistic Regression**| 0.6369 | 0.6339 | 0.6309 | 0.6258 | 0.6307 | **0.63164** | ±0.00415 | 0.00185 | `[0.62650, 0.63679]` |

* **Nested Cross-Validation vs. Holdout Validation:**  
  When hyperparameter tuning is conducted across cross-validation folds, a nested cross-validation architecture is necessary to prevent optimistic selection bias. In our workflow, hyperparameters and operational thresholds were fixed using the independent 10,000-record validation set. Therefore, executing a separate 5-fold Stratified CV on the 70,000 training records provides an out-of-fold generalization check on fixed architectures with within-fold preprocessing, avoiding the massive computational overhead of nested tuning while preventing tuning leakage.
* **Limitations of 5-Fold Variance Estimation & Independence Caveat:**  
  Five folds provide limited sample degrees of freedom ($df = 4$), necessitating Student's $t$-distribution ($t_{0.975, 4} = 2.776$) rather than standard normal $Z$-critical values. Furthermore, as rigorously demonstrated by Bengio & Grandvalet (2004), because training folds share $75\%$ of their data, cross-validation errors are correlated, meaning naive sample standard errors underestimate true prediction error variance. Consequently, fold-based intervals reflect descriptive fold-to-fold variation and **must not be interpreted as fully independent statistical confidence intervals**.
* **Why Monotonic Transformations Do Not Expand Tree Capacity:**  
  Decision trees evaluate univariate split candidates based on rank order. Strictly monotonic transformations (such as $f(x) = \log(1+x)$) preserve the relative ordering of feature values ($x_a < x_b \iff f(x_a) < f(x_b)$), leaving the set of possible binary partitions on any single continuous feature mathematically identical.

---

### 3. Model Comparison, Reproducibility Status & Latency Benchmarks
On the 20,000 reserved test partition, candidate models achieved the following performance:

| Model | Val AUC | Test AUC | Accuracy | Recall | Precision | Operational Rationale |
|:------|:-------:|:--------:|:--------:|:------:|:---------:|:----------------------|
| **Tri-Blend Benchmark (50/30/20)** | **0.7052** | **0.7019** | 64.39% | 64.94% | 63.83% | **Benchmark:** Performance upper bound; 3x ops overhead |
| **Tuned LightGBM V3 (Champion)** | **0.7051** | **0.7015** | **64.38%** | **64.93%** | **63.82%** | **Champion:** Single dependency, fast inference, native TreeSHAP |
| **Tuned XGBoost V3** | 0.7011 | 0.6981 | 63.70% | 64.17% | 63.17% | Depth-wise tree growth benchmark |
| **Baseline LightGBM** | 0.7008 | 0.6979 | 64.05% | 64.91% | 63.42% | Initial walkthrough baseline |
| **CatBoost V3** | 0.7000 | 0.6973 | 63.90% | 64.31% | 63.38% | Oblivious tree architecture benchmark |
| **Scaled Logistic Regression** | 0.6405 | 0.6395 | 59.83% | 58.59% | 59.64% | Linear baseline |

* **Paired Model Significance Test (Tri-Blend vs. Tuned LightGBM V3):**  
  On the 20,000 reserved test set, the observed difference between Tri-Blend (0.7019) and Tuned LightGBM V3 (0.7015) is +0.0004. Because individual test-set predictions were not serialized to disk, formal test-set paired statistical significance (such as a DeLong test) is unverified from static artifacts, and no numerical significance p-value is claimed. Across the 5 cross-validation folds on the training set (oof_predictions_v3.csv), the mean fold AUC difference is +0.00157 (0.7026 vs. 0.7011). Tuned LightGBM V3 is selected as the Champion Model for the PoC based on operational simplicity, a single runtime dependency, and native C++ TreeSHAP attribution.
* **Operational Justification & Latency Qualification:**  
  Tuned LightGBM V3 executes within a single runtime dependency (`lightgbm`) and supports native C++ TreeSHAP attribution. Single-record prediction latencies (~0.38-1.08 ms for LightGBM V3, ~2.15 ms for Tri-Blend) and TreeSHAP latency (~1.0 ms) are unverified preliminary developmental observations and must NOT be interpreted as certified production benchmarks.

---

## 💼 Business Proposal: Precision Retention Programme (PRP)

Using the champion model's risk thresholds on predicted churn probabilities (note: no post-hoc Platt scaling or isotonic calibration was applied), subscribers are segmented into three operational tiers:

1. **Red Tier ($p \ge 0.70$): High Risk**
   - **Intervention:** **Handset Upgrade & 2-Year Contract Renewal.** Subsidize a new 5G-capable handset ($60 credit) paired with proactive VIP outbound concierge outreach ($20 cost) = **$80/customer**.
   - **Target Volume:** 2,351 test customers (11.76%) | 11,755 fleet customers. Churn rate: 78.60%.
   - **Rationale:** Churners hold devices 58 days older on average. Upgrading the device eliminates handset fatigue and secures a 24-month contract renewal.
2. **Amber Tier ($0.50 \le p < 0.70$): Moderate Risk**
   - **Intervention:** **Automated Plan Right-Sizing & Overage Relief.** Automated SMS and in-app prompts recommending plan adjustments to eliminate billing overage penalties = **$15/customer**.
   - **Target Volume:** 7,734 test customers (38.67%) | 38,670 fleet customers. Churn rate: 59.32%.
   - **Rationale:** High overage revenue ratio signals "bill shock," which triggers provider switching.
3. **Green Tier ($p < 0.50$): Low Risk**
   - **Intervention:** Standard service nurturing; zero incremental outreach spend. Monthly automated re-scoring.
   - **Target Volume:** 9,915 test customers (49.58%) | 49,575 fleet customers. Churn rate: 35.06%.

### Expected Economic Value (EV) Decision Rule & Metric Distinction

To avoid metric confusion between conditional response rates and experimental treatment lift:
1. **Conditional Retention Response Rate ($r$):** The proportion of impending churners saved by the intervention (scenario assumptions: $r_{\text{Red}} = 25.0\%$, $r_{\text{Amber}} = 15.0\%$).
2. **Absolute Churn-Rate Reduction ($\Delta_{\text{churn}}$):** In a randomized trial, the observable difference between control and treatment churn rates is:
   $$\Delta_{\text{churn}} = p_{\text{control}} \times r$$
3. **Incremental Net EBITDA Contribution per Treated Customer:**
   $$\Delta_{\text{EBITDA}} = \Delta_{\text{churn}} \times (\text{LTV} \times M_{\text{EBITDA}}) - C$$
   Under an assumed 50% EBITDA margin benchmark ($LTV_{\text{EBITDA}} = \$450$), break-even occurs when $\Delta_{\text{churn, BE}} = C / \$450$:
   - **Red Tier Break-Even:** $\Delta_{\text{churn, BE, Red}} = \$80 / \$450 = \mathbf{17.78 \text{ percentage points}}$ (corresponding to conditional response $r_{\text{BE}} = 17.78\% / 78.60\% = \mathbf{22.62\%}$).
   - **Amber Tier Break-Even:** $\Delta_{\text{churn, BE, Amber}} = \$15 / \$450 = \mathbf{3.33 \text{ percentage points}}$ (corresponding to conditional response $r_{\text{BE}} = 3.33\% / 59.32\% = \mathbf{5.62\%}$).

### Phase 1 Randomized Controlled Trial (A/B Testing Pilot Design) & Statistical Power
Before committing the full fleet budget ($1.52M), a Phase 1 A/B pilot is conducted:
- **Primary Endpoint:** 90-day binary churn status.
- **Analysis Framework:** Intention-to-Treat (ITT).
- **Dedicated Red Pilot ($N = 3,000$, 80/20 Allocation):** MDE = **5.29 percentage points**; power **>99.9%** to detect the 17.78 pp break-even effect (note: the earlier 5.29-5.59 pp range in exploratory scripts was due to an inverted sample ratio calculation).
- **Dedicated Amber Pilot ($N = 7,000$, 50/50 Balanced Allocation):** MDE = **3.31 percentage points**; power = **~80.6%** to detect the 3.33 pp break-even effect. Sample size requirement: **6,840-6,896 subscribers** (unpooled normal) or **7,020 subscribers** (Fleiss with continuity correction).

### Financial Impact: Retrospective vs. Prospective Audited Model

To avoid conflating historical test-set evaluation with live campaign forecasting, results are disaggregated into two distinct frameworks:

#### 1. Prospective Model-Driven Forecast (Live Operational Deployment)
Expected churners are estimated by summing model-predicted probabilities within each tier (Red: $\sum \hat{p}_i = 1,840.35$; Amber: $\sum \hat{p}_i = 4,563.29$). Retained subscribers are projected using hypothetical response rate assumptions (25% Red, 15% Amber per McKinsey, 2023 [5]):
- **Held-Out Test Set ($n = 20,000$):**
  - **Red Tier:** 2,351 targeted | 1,840.35 expected churners (78.28%) | **460.09 retained** (disp. 460) | Cost: $188,080.
  - **Amber Tier:** 7,734 targeted | 4,563.29 expected churners (59.00%) | **684.49 retained** (disp. 684) | Cost: $116,010.
  - **Total Retained:** **1,144.58 expected subscribers** (disp. 1,145) | Cost: $304,090.
  - **Gross Revenue Protected:** **$1,030,124.14** ($1,144.58 \times \$900$ LTV) | Net Revenue: **$726,034.14** (Net Rev ROI: **238.76%**).
  - **Estimated EBITDA Contribution (50% Margin):** **$515,062.07**; Net EBITDA: **$210,972.07** (EBITDA ROI: **69.38%**).
- **Enterprise Fleet ($n = 100,000$, Scaled $5.0\times$):**
  - **Red Tier:** 11,755 targeted | 9,201.75 expected churners | **2,300.44 retained** (disp. 2,300) | Cost: $940,400.
  - **Amber Tier:** 38,670 targeted | 22,816.45 expected churners | **3,422.47 retained** (disp. 3,422) | Cost: $580,050.
  - **Total Fleet Retained:** **5,722.91 expected subscribers** (disp. 5,723) | Cost: $1,520,450.
  - **Gross Revenue Protected:** **$5,150,620.70** | Net Protected Revenue: **$3,630,170.70** (Net Rev ROI: **238.76%**; Gross multiple: **338.76% / 3.39x**).
  - **Estimated EBITDA Contribution (50% Margin):** **$2,575,310.35**; Net EBITDA: **$1,054,860.35** (EBITDA ROI: **69.38%**).
  - **Break-Even EBITDA Margin:** **29.52%**.

#### 2. Retrospective Evaluation Scenario (Observed Ground-Truth Labels)
Evaluates historical test-set performance using actual observed churn labels (1,848 Red churners, 4,588 Amber churners):
- **Held-Out Test Set ($n = 20,000$):**
  - **Red Tier:** 1,848 actual churners | **462.00 retained** (disp. 462) | Cost: $188,080.
  - **Amber Tier:** 4,588 actual churners | **688.20 retained** (disp. 688) | Cost: $116,010.
  - **Total Retained:** **1,150.20 expected subscribers** (disp. 1,150) | Cost: $304,090.
  - **Gross Revenue Protected:** **$1,035,180.00** | Net Revenue: **$731,090.00** (Net Rev ROI: **240.42%**).
  - **Estimated EBITDA Contribution (50% Margin):** **$517,590.00**; Net EBITDA: **$213,500.00** (EBITDA ROI: **70.21%**).
- **Enterprise Fleet ($n = 100,000$, Scaled $5.0\times$):**
  - **Total Fleet Retained:** **5,751.00 expected subscribers** (disp. 5,751) | Cost: $1,520,450.
  - **Gross Revenue Protected:** **$5,175,900.00** | Net Protected Revenue: **$3,655,450.00** (Net Rev ROI: **240.42%**; Gross multiple: **340.42% / 3.40x**).
  - **Estimated EBITDA Contribution (50% Margin):** **$2,587,950.00**; Net EBITDA: **$1,067,500.00** (EBITDA ROI: **70.21%**).
  - **Break-Even EBITDA Margin:** **29.38%**.
- **Full Baseline Reconciliation:** Baseline segmentation (2,094 Red / 7,940 Amber) retained 5,596 subscribers, generating $3.60M net revenue, 251.42% Net Rev ROI, 351.42% Gross Ratio, and $1.08M net EBITDA. Champion LightGBM V3 targets 257 more high-risk customers, securing +155 more subscribers and +$52.4k more net cash, shifting Net Rev ROI to 240.42% due to higher base capital deployment.

---

## 🚀 How to Reproduce

### 1. Environment Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Execute Analysis Notebook
```bash
python3 -m nbconvert --to notebook --execute --inplace notebooks/analysis.ipynb
```

### 3. Generate Executive Presentation PDF
```bash
python3 src/generate_presentation.py
```

---

## 📋 Omnicampus Submission Checklist

1. **Slide File Naming:** `[OmnicampusAccountName].pdf` — Verified size: **892 KB** across exactly **15 slides**.
2. **Notebook File Naming:** `[OmnicampusAccountName].ipynb` — Verified clean execution across 30 cells with all outputs intact.
3. **List of References Field:** Copy contents of [`reports/references.md`](reports/references.md).
4. **Generative AI Chat URL:** `https://gemini.google.com/share/8f3373e04b344d08a5a6c67c1332d860` (Conversation ID: `8f3373e0-4b34-4d08-a5a6-c67c1332d860`).

---

*GCI World 2026 September Final Assignment | Company A Telecommunications | All Rights Reserved*
