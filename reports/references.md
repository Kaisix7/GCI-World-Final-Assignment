# References & Literature Audit

## GCI World 2026 September Final Assignment — Company A Telecom Churn Analysis

This document provides the audited inventory of all references, external benchmarks, course resources, and scenario assumptions utilized throughout the Company A Churn Prediction and Retention Strategy PoC.

To maintain strict academic integrity and methodological transparency, all sources are categorized by their epistemic status:
1. **Peer-Reviewed Academic Literature** (canonical DOI/journal links).
2. **Industrial Market Context & Regulatory Publications** (qualified macro industry context).
3. **Official GCI World Course Materials & Dataset Documentation** (local course files).
4. **Hypothetical Scenario Assumptions** (explicitly unverified scenario modeling parameters).

---

### Category 1: Peer-Reviewed External Academic Literature

[1] **Reichheld, F. F., & Schefter, P. (2000).** *E-loyalty: Your secret weapon on the web.* **Harvard Business Review**, 78(4), 105–113.  
* **Canonical URL:** https://hbr.org/2000/07/e-loyalty-your-secret-weapon-on-the-web  
* **Verification Status:** Verified [HTTP 200]. Canonical publication on relationship marketing economics.  
* **Claim Supported:** Acquiring a new customer costs 5–7× more than retaining an existing subscriber; a 5% increase in retention lifts customer lifetime profitability by 25–95%. Cited on Slide 1, 3, 13, 14, and 15.

[7] **Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., Ye, Q., & Liu, T. Y. (2017).** *LightGBM: A highly efficient gradient boosting decision tree.* **Advances in Neural Information Processing Systems (NeurIPS 30)**, 3146–3154.  
* **Canonical URL:** https://papers.nips.cc/paper/2017/hash/6449f44a102fde848669bdd9eb6b76fa-Abstract.html  
* **Verification Status:** Verified [HTTP 200]. Original peer-reviewed publication for LightGBM.  
* **Claim Supported:** Validates Gradient-based One-Side Sampling (GOSS), Exclusive Feature Bundling (EFB), and leaf-wise histogram tree growth used by the Champion Model (Tuned LightGBM V3). Cited on Slide 8, 9, 10, 11, and 15.

[8] **Chen, T., & Guestrin, C. (2016).** *XGBoost: A scalable tree boosting system.* **Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining**, 785–794.  
* **Canonical DOI:** https://doi.org/10.1145/2939672.2939785  
* **Verification Status:** Verified [HTTP 200]. Canonical peer-reviewed paper for XGBoost.  
* **Claim Supported:** Validates second-order Taylor approximation split-finding for gradient boosted decision trees used in XGBoost V2/V3 benchmark models. Cited on Slide 8, 9, 10, and 15.

[9] **Prokhorenkova, L., Gusev, G., Vorobev, A., Dorogush, A. V., & Gulin, A. (2018).** *CatBoost: unbiased boosting with categorical features.* **Advances in Neural Information Processing Systems (NeurIPS 31)**, 6638–6648.  
* **Canonical URL:** https://papers.nips.cc/paper/2018/hash/14491b756b3a51daac41c24863285549-Abstract.html  
* **Verification Status:** Verified [HTTP 200]. Canonical peer-reviewed paper for CatBoost.  
* **Claim Supported:** Evaluates ordered boosting and oblivious decision trees on target statistics to combat prediction shift on categorical features. Cited on Slide 8, 9, 10, and 15.

[10] **Lundberg, S. M., & Lee, S. I. (2017).** *A unified approach to interpreting model predictions.* **Advances in Neural Information Processing Systems (NeurIPS 30)**, 4765–4774.  
* **Canonical URL:** https://papers.nips.cc/paper/2017/hash/8a20a8621978632d76c43dfd28b67767-Abstract.html  
* **arXiv Preprint:** https://arxiv.org/abs/1705.07874  
* **Verification Status:** Verified [HTTP 200]. Seminal game-theoretic TreeSHAP interpretability paper.  
* **Claim Supported:** Mathematical foundation for TreeSHAP local attribution and global importance interpretation without causal extrapolation. Cited on Slide 7, 10, and 15.

[11] **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine learning in Python.* **Journal of Machine Learning Research**, 12, 2825–2830.  
* **Canonical URL:** https://jmlr.csail.mit.edu/papers/v12/pedregosa11a.html  
* **Verification Status:** Verified [HTTP 200]. Canonical journal publication for scikit-learn.  
* **Claim Supported:** Standard reference for stratified data splitting (`StratifiedKFold`), preprocessing scalers (`StandardScaler`), logistic regression, and ROC-AUC evaluation. Cited on Slide 4, 8, 9, and 15.

[14] **Bengio, Y., & Grandvalet, Y. (2004).** *No unbiased estimator of the variance of K-fold cross-validation.* **Journal of Machine Learning Research**, 5, 1089–1105.  
* **Canonical URL:** https://www.jmlr.org/papers/v5/grandvalet04a.html  
* **Verification Status:** Verified [HTTP 200]. Foundational statistical paper on cross-validation variance.  
* **Claim Supported:** Theoretical justification explaining why standard paired t-tests across CV folds underestimate variance due to training-set overlap, motivating reserved test evaluation and the reporting of descriptive rather than inferential confidence intervals on 5-fold CV scores. Cited in README Section 2 and Notebook Section 4.

[15] **DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988).** *Comparing the areas under two or more correlated receiver operating characteristic curves: a nonparametric approach.* **Biometrics**, 44(3), 837–845.  
* **Canonical DOI:** https://doi.org/10.2307/2531595  
* **Verification Status:** Verified [HTTP 200]. Mathematical foundation for non-parametric correlated ROC-AUC variance.  
* **Claim Supported:** Theoretical formulation for the paired AUC comparison test. **Explicit Disclosure:** Because individual test-set predictions were not serialized to disk, formal test-set DeLong inference is unverified from static files and no numerical test p-value is claimed. Cited on Slide 10, README Section 3, and Notebook Section 4.

[16] **Fleiss, J. L., Levin, B., & Paik, M. C. (2003).** *Statistical Methods for Rates and Proportions (3rd Edition).* John Wiley & Sons.  
* **Canonical DOI:** https://doi.org/10.1002/0471445428  
* **Verification Status:** Verified [HTTP 200]. Standard textbook on proportion testing.  
* **Claim Supported:** Provides the two-sample proportion sample size formula with continuity correction ($N = 7,020$ total required for Amber pilot to detect a 3.33 percentage point reduction at 80% power). Cited on Slide 14, README Section 4, and Notebook Section 6.

[17] **Chow, S. C., Shao, J., Wang, H., & Lokhnygina, Y. (2017).** *Sample Size Calculations in Clinical Research (3rd Edition).* Chapman and Hall/CRC.  
* **Canonical DOI:** https://doi.org/10.1201/9781315183084  
* **Verification Status:** Verified [HTTP 200]. Authoritative reference on trial power and MDE calculations.  
* **Claim Supported:** Unpooled normal approximation formulas for two-sample proportion tests establishing MDE = 5.29 percentage points for the Red pilot ($N=3,000$, 80/20 allocation) and MDE = 3.31 percentage points for the Amber pilot ($N=7,000$, 50/50 allocation). Cited on Slide 14, README Section 4, and Notebook Section 6.

---

### Category 2: Industrial Market Context & Regulatory Publications (Qualified External Sources)

[2] **CTIA — The Wireless Association. (2024).** *Annual Wireless Industry Survey: 2024 Results & Trends.* CTIA Research.  
* **Canonical URL:** https://www.ctia.org/news/annual-wireless-industry-survey-2024  
* **Verification Status:** Verified [HTTP 200]. Authoritative trade association representing the US wireless communications industry.  
* **Direct Page / Passage:** Public release tracks 558M+ active US wireless connections and record wireless data volume (100+ trillion MB). Granular postpaid ARPU tables are compiled in CTIA's proprietary *Wireless Industry Indices Report*.  
* **Claim Supported & Explicit Qualification:** Contextualizes the \$45–\$55 monthly blended postpaid ARPU range in US telecommunications. **Qualification:** The exact \$50.00 ARPU baseline (\$900 18-month contractual LTV) is an **illustrative scenario assumption** informed by industry indices, not a public data point printed in this release. Cited on Slide 1, 3, 13, 14, and 15.

[3] **GSMA Intelligence. (2024).** *The Mobile Economy 2024.* GSMA Intelligence Research.  
* **Canonical URL:** https://www.gsmaintelligence.com/research/2024/02/the-mobile-economy-2024/  
* **Verification Status:** Verified [HTTP 200]. Global mobile operator research clearinghouse.  
* **Direct Page / Passage:** Flagship report covers global mobile penetration, 5G adoption, and consumer switching behavior (~14% annual provider switching rate across analyzed markets).  
* **Claim Supported & Explicit Qualification:** Provides macro context for carrier switching rates in mature mobile markets. **Qualification:** The 1.5%–3.0% monthly carrier churn range is an **illustrative industry operating benchmark**; Company A's monthly baseline churn (1.94% monthly) is evaluated against this standard operating range. Cited on Slide 3 and Slide 15.

[4] **Ericsson ConsumerLab. (2024).** *Ericsson Mobility Report (November 2024 Edition).* Ericsson.  
* **Canonical URL:** https://www.ericsson.com/en/reports-and-papers/mobility-report/reports/november-2024  
* **Verification Status:** Verified [HTTP 200]. Canonical report tracking global mobile traffic and network transitions.  
* **Direct Page / Passage:** Analyzes 5G subscriber growth (surpassing 2 billion globally), traffic share, and the acceleration of device upgrades toward 5G-capable handsets.  
* **Claim Supported & Explicit Qualification:** Contextualizes handset replacement cycles in mature networks. **Qualification:** The specific variable `eqpdays` (equipment age) and the finding that churn risk sharply increases after 300–400 days are **empirical findings directly derived from Company A's dataset**, not empirical assertions from Ericsson. Cited on Slide 3, 6, 12, and 15.

[6] **Federal Communications Commission (FCC). (2024).** *2024 Communications Marketplace Report (FCC 24-136).* Federal Communications Commission.  
* **Canonical URL:** https://www.fcc.gov/document/2024-communications-marketplace-report  
* **Verification Status:** Verified [Official US Government Document]. Biennial report to Congress on mobile wireless competition.  
* **Direct Page / Passage:** Section III examines consumer wireless competition, data caps, overages, and churn metrics as indicators of switching friction and market competition.  
* **Claim Supported & Explicit Qualification:** Contextualizes billing friction and data caps under consumer protection frameworks. **Qualification:** The finding that overage fees (`overage_rev_ratio`) and customer service friction (`service_friction_index`) are leading empirical churn drivers is an **empirical finding directly from Company A's data and TreeSHAP analysis**, not an empirical claim made by the FCC regarding Company A. Cited on Slide 8, 12, and 15.

---

### Category 3: Official GCI World Course Materials & Dataset Documentation (Local Course Files)

[12] **GCI World Instruction Team. (2026).** *GCI World 2026 September Final Assignment Tutorial: Baseline Preprocessing and Modeling Protocol (`tutorial.ipynb`).*  
* **Location:** Local course file `tutorial.ipynb` (workspace root).  
* **Verification Status:** Verified [Local File Intact]. Primary course instructional artifact.  
* **Claim Supported:** Establishes the official assignment baseline pipeline: raw column mappings, missing value imputation conventions, 80/20 train/test partition (`random_state=42`), and baseline LightGBM model configuration ($ROC\text{-}AUC \approx 0.6981$ CV, $0.6968$ test). Cited on Slide 4, 8, 9, 10, and 15.

[13] **GCI World Course Administration. (2026).** *Company A Telecommunications Churn Dataset Overview and Field Dictionary (`ENG_Company_A_Dataset_Overview.docx`).*  
* **Location:** Local course file `ENG_Company_A_Dataset_Overview.docx` (workspace root).  
* **Verification Status:** Verified [Local File Intact]. Official course dataset documentation.  
* **Claim Supported:** Authoritative field dictionary defining all 69 tabular columns across `Client.csv` and `Record.csv`, confirming operational definitions of churn, tenure, billing variables, and customer care interaction fields. Cited on Slide 4 and Slide 15.

---

### Category 4: Hypothetical Scenario Assumptions (No External Empirical Citation)

The following parameters are **hypothetical scenario assumptions** designed for operational business modeling. They do not possess empirical academic citations and are explicitly documented as modeling scenarios:

[5] **Retention Campaign Response Rates (25% Red Tier / 15% Amber Tier):**  
* **Literature Reference Context:** McKinsey & Company (2023), *Why AI-enabled customer service is key to scaling telco personalization* (https://www.mckinsey.com/industries/technology-media-and-telecommunications/our-insights/why-ai-enabled-customer-service-is-key-to-scaling-telco-personalization). Recommends proactive next-best-experience AI engines and personalized retention interventions.  
* **Epistemic Status:** **Hypothetical Scenario Assumption**.  
* **Explicit Disclosure:** The specific response rates of 25% for high-risk subscribers (Red Tier) and 15% for moderate-risk subscribers (Amber Tier) are hypothetical scenario parameters. They are not empirical findings for Company A. A Phase 1 randomized controlled trial (A/B testing pilot) is explicitly required to measure actual empirical response before enterprise rollout.

* **Illustrative Postpaid ARPU Baseline (\$50.00 / month):**  
  * **Epistemic Status:** Scenario modeling parameter. Informed by general US wireless industry ranges ($45–$55) reported in CTIA surveys, but treated as an unverified illustrative baseline. Gross 18-month contractual LTV = \$900.00.

* **Illustrative Enterprise EBITDA Margin (50.0%):**  
  * **Epistemic Status:** Financial modeling benchmark. Industry rule of thumb used to translate gross preserved revenue into operating contribution. Break-even EBITDA operating margins are explicitly calculated as **29.52%** (prospective) and **29.38%** (retrospective).

* **Developmental Latency Benchmarks (0.38–1.08 ms LightGBM V3, 2.15 ms Tri-Blend):**  
  * **Epistemic Status:** Preliminary developmental observation. Profiled on local host hardware (Apple Silicon ARM64, Python runtime) on single-record evaluation; not a contracted enterprise SLA.

---

### Generative AI Conversation Disclosure

In accordance with official GCI World Final Assignment transparency guidelines:

* **Tool Utilized:** Antigravity (Powered by Claude Sonnet & Gemini)
* **Scope of Assistance:**
  1. Methodological audit of cross-validation splits, leakage prevention, and paired significance testing.
  2. Reconciliation of prospective vs. retrospective financial equations.
  3. Formulation of exact unpooled normal and Fleiss continuity-corrected sample size calculations.
  4. Generation of production deliverables (FPDF2 slide generation script, clean executed Jupyter notebook, and documentation).
* **Integrity Statement:** All empirical metrics, model validation scores, confusion matrices, and financial projections are computed directly from Company A's raw dataset (`Client.csv` and `Record.csv`). Zero metrics or citations have been fabricated.
* **Conversation ID:** `8f3373e0-4b34-4d08-a5a6-c67c1332d860`
* **Shareable URL for Submission:**  
  > **`[Student to insert verified AI conversation history URL here]`**
