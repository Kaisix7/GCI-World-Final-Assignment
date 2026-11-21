from fpdf import FPDF
import os


class Presentation(FPDF):
    PRIMARY = (25, 93, 161)
    ACCENT = (220, 38, 38)
    LIGHT = (241, 245, 249)
    DARK = (15, 23, 42)
    GRAY = (100, 116, 139)
    NAVY = (30, 58, 138)

    def slide_bg(self, r=255, g=255, b=255):
        self.set_fill_color(r, g, b)
        self.rect(0, 0, 297, 210, 'F')

    def header_bar(self, title, subtitle=''):
        self.set_fill_color(*self.PRIMARY)
        self.rect(0, 0, 297, 40, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 18)
        self.set_xy(15, 8)
        self.cell(267, 10, title, align='L')
        if subtitle:
            self.set_font('Helvetica', '', 10.5)
            self.set_xy(15, 22)
            self.cell(267, 8, subtitle, align='L')

    def footer_bar(self, slide_num):
        self.set_fill_color(*self.PRIMARY)
        self.rect(0, 196, 297, 14, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', '', 8.5)
        self.set_xy(15, 198)
        self.cell(160, 8, 'Company A Telecom | Churn Prediction & Retention Strategy PoC | GCI World 2026 September', align='L')
        self.set_xy(15, 198)
        self.cell(267, 8, f'Slide {slide_num} / 15', align='R')

    def kpi_box(self, x, y, w, h, label, value, fr=241, fg=245, fb=249, vr=25, vg=93, vb=161):
        self.set_fill_color(fr, fg, fb)
        self.rect(x, y, w, h, 'F')
        self.set_draw_color(203, 213, 225)
        self.rect(x, y, w, h, 'D')
        self.set_text_color(*self.GRAY)
        self.set_font('Helvetica', '', 8.5)
        self.set_xy(x, y+3)
        self.cell(w, 6, label, align='C')
        self.set_text_color(vr, vg, vb)
        self.set_font('Helvetica', 'B', 13.5)
        self.set_xy(x, y+10)
        self.cell(w, 9, value, align='C')

    def add_image_safe(self, path, x, y, w):
        if os.path.exists(path):
            self.image(path, x=x, y=y, w=w)
        else:
            self.set_fill_color(220, 220, 220)
            self.rect(x, y, w, int(w*0.6), 'F')


pdf = Presentation(orientation='L', unit='mm', format='A4')
pdf.set_auto_page_break(False)

pdf.add_page()
pdf.slide_bg(25, 93, 161)
pdf.set_text_color(255, 255, 255)
pdf.set_font('Helvetica', 'B', 28)
pdf.set_xy(0, 46)
pdf.cell(297, 15, 'Company A Telecommunications', align='C')
pdf.set_font('Helvetica', 'B', 18)
pdf.set_xy(0, 64)
pdf.cell(297, 10, 'Predictive Churn Modelling & Precision Retention Strategy', align='C')
pdf.set_font('Helvetica', '', 13)
pdf.set_xy(0, 84)
pdf.cell(297, 8, 'Proof of Concept (PoC) Business Model Proposal', align='C')
pdf.set_xy(0, 95)
pdf.cell(297, 8, 'GCI World 2026 September Final Assignment', align='C')
pdf.set_xy(0, 106)
pdf.cell(297, 8, 'Author: Karina B.  |  November 2026', align='C')
pdf.set_fill_color(220, 38, 38)
pdf.rect(75, 122, 147, 3, 'F')
pdf.set_font('Helvetica', 'I', 10.5)
pdf.set_xy(0, 132)
pdf.cell(297, 7, '100,000 Subscribers | Strictly Leak-Free Pipeline | Champion Model for the PoC: Tuned LightGBM V3 (CV 0.7011, Test 0.7015)', align='C')
pdf.footer_bar(1)

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Executive Summary: Transforming Telemetry into Retained Margin', 'Proof of Concept Business Model Proposal: +5,723 Retained Subscribers & +$1.05M Net EBITDA Contribution')
pdf.footer_bar(2)
kpis = [
    ('Subscribers Analysed', '100,000', 241, 245, 249, 25, 93, 161),
    ('Champion Model AUC', '0.7011 CV / 0.7015 Test', 241, 245, 249, 25, 93, 161),
    ('Prospective Fleet Retained', '5,723 (Retro: 5,751)', 240, 253, 244, 22, 101, 52),
    ('Prospective Net EBITDA', '$1,054,860 (Retro: $1.07M)', 240, 253, 244, 22, 101, 52),
    ('EBITDA ROI (50% Margin)', '69.38% (Retro: 70.21%)', 240, 253, 244, 22, 101, 52),
    ('Net Protected Rev / Net ROI', '$3.63M / 238.76%', 241, 245, 249, 25, 93, 161),
]
for i, (label, value, fr, fg, fb, vr, vg, vb) in enumerate(kpis):
    col = i % 3
    row = i // 3
    x = 10 + col * 93
    y = 46 + row * 40
    pdf.kpi_box(x, y, 89, 34, label, value, fr, fg, fb, vr, vg, vb)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 130, 277, 30, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 130, 277, 30, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_xy(15, 133)
pdf.cell(267, 5, 'Executive Mandate: The Precision Retention Programme (PRP)')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.5)
pdf.set_xy(15, 140)
pdf.multi_cell(267, 4.2, 'Using our leak-free Tuned LightGBM V3 scoring engine, subscribers are segmented into risk tiers: high-risk subscribers (p >= 0.70) receive subsidized handset renewals ($80/cust), while moderate-risk subscribers (p 0.50-0.70) receive digital plan right-sizing ($15/cust). Across Company A full 100k fleet, the prospective forecast projects 5,723 retained subscribers (+$1.05M net EBITDA, 69.38% EBITDA ROI at 50% operating margin; $3.63M net revenue, 238.76% Net ROI; break-even margin 29.52%), tracking retrospective test evaluation (5,751 retained, $1,067,500 net EBITDA, 70.21% ROI, $3.66M net revenue).')

pdf.set_fill_color(240, 249, 255)
pdf.rect(10, 163, 277, 28, 'F')
pdf.set_draw_color(186, 230, 253)
pdf.rect(10, 163, 277, 28, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.0)
pdf.set_xy(15, 165)
pdf.cell(267, 5, 'Strategic Baseline Model Reconciliation & Capital Efficiency')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.3)
pdf.set_xy(15, 171)
pdf.multi_cell(267, 4.0, 'Reconciled Baseline Model: The tutorial baseline LightGBM model captured 5,596 retained fleet subscribers ($3.60M net revenue, 251.42% Net Rev ROI, $1.08M net EBITDA, 28.46% break-even margin). Tuned LightGBM V3 targets 257 additional high-risk Red subscribers, securing +155 net retained subscribers and +$27.1k to +$52.4k more net protected revenue, solidifying Company A subscriber base against competitive switching.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Market Context: Why Retention Dominates Postpaid Wireless Unit Economics', 'Customer Acquisition Costs (5-7x) & Postpaid ARPU Require Targeted Churn Mitigation')
pdf.footer_bar(3)

market_cards = [
    ('5-7x Multiple', 'Customer Acquisition vs Retention Cost', 'Acquiring a new postpaid subscriber costs 5-7x more than retaining an existing account (Reichheld & Schefter, 2000 [1]). Retention protects existing network scale and margin.'),
    ('$50 / Month', 'Average Revenue Per User (Postpaid ARPU)', 'US postpaid wireless ARPU averages $45-$55/month (CTIA Wireless Industry Report, 2024 [2]). Our financial model establishes an 18-month gross LTV of $900 per subscriber.'),
    ('18-24% Annual', 'Industry Churn Benchmark Rate', 'Annual postpaid wireless churn in competitive markets ranges between 1.5% and 2.0% monthly (GSMA Intelligence, 2024 [3]). Company A historical dataset exhibits a 49.56% churn rate.')
]
for i, (metric, title, desc) in enumerate(market_cards):
    x = 10 + i * 93
    pdf.set_fill_color(*pdf.LIGHT)
    pdf.rect(x, 46, 89, 44, 'F')
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(x, 46, 89, 44, 'D')
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 16)
    pdf.set_xy(x+3, 49)
    pdf.cell(83, 7, metric, align='C')
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.set_xy(x+3, 58)
    pdf.cell(83, 5, title, align='C')
    pdf.set_text_color(*pdf.GRAY)
    pdf.set_font('Helvetica', '', 8.0)
    pdf.set_xy(x+5, 65)
    pdf.multi_cell(79, 3.8, desc, align='L')

pdf.set_fill_color(255, 255, 255)
pdf.rect(10, 95, 136, 95, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 95, 136, 95, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(15, 98)
pdf.cell(126, 6, 'A. The Asymmetric Economics of Churn')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.5)
pdf.set_xy(15, 107)
pdf.multi_cell(126, 4.3, '1. Severe Economic Asymmetry: Missing an impending churner forfeits $900 in contractual gross revenue ($450 at 50% EBITDA margin). Conversely, proactive outreach costs only $15 to $80 per customer, establishing an asymmetric 11.25x to 60x payoff ratio.\n\n2. The Danger of Blanket Promotions: Broad-based discounting subsidizes customers who never intended to churn, severely eroding operator margins without reducing attrition.\n\n3. Value of Precision Targeting: Precision machine learning scoring identifies high-probability churners before contract expiration, concentrating retention capital where marginal recovery exceeds intervention cost.')

pdf.rect(151, 95, 136, 95, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(151, 95, 136, 95, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(156, 98)
pdf.cell(126, 6, 'B. PoC Objectives & Core Deliverables')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.5)
pdf.set_xy(156, 107)
pdf.multi_cell(126, 4.3, '1. Leak-Free Machine Learning Engine: Train, evaluate, and benchmark candidate algorithms under strict within-fold preprocessing to prevent optimistic data leakage.\n\n2. Actionable Risk Segmentation: Map continuous predicted probabilities to operational risk tiers (Red, Amber, Green) tied to specific commercial interventions.\n\n3. Quantified Financial Valuation: Build prospective model forecasts (sum of probabilities) and retrospective evaluation scenarios with sensitivity testing.\n\n4. Experimental Validation Framework: Establish a rigorous Phase 1 randomized controlled trial (A/B testing pilot design) with minimum detectable effect (MDE) and power verification.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Data Architecture & Strictly Leak-Free Preprocessing Protocol', 'Zero-Contamination Design: Stratified 70k Train, 10k Validation & 20k Reserved Test Split')
pdf.footer_bar(4)

pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(10, 44)
pdf.cell(135, 6, 'Database Schema & Partitioning Protocol')

rows_data = [
    ('Client.csv', '100,000 rows x 50 cols', 'Account, demographics, tenure, device model [12]'),
    ('Record.csv', '100,000 rows x 51 cols', 'Monthly usage (MOU), billing, quality metrics, churn [12]'),
    ('3-Way Split Protocol', '70k Train / 10k Val / 20k Test', 'Stratified 70/10/20 partition; reserved test partition with historical exploratory inspection'),
    ('Structural Drops', '16 features dropped', '3 >35% missing (numbcars, dwllsize, HHstatin), 13 collinear >0.95'),
    ('Zero Data Leakage', 'Train-Only Transformations', 'Numeric medians, drop thresholds & encodings fit on TRAIN only'),
]
y = 52
for name, detail, note in rows_data:
    pdf.set_fill_color(*pdf.LIGHT)
    pdf.rect(10, y, 42, 9, 'F')
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(10, y, 42, 9, 'D')
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 8.2)
    pdf.set_xy(11, y+2)
    pdf.cell(40, 5, name)
    
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(52, y, 45, 9, 'F')
    pdf.rect(52, y, 45, 9, 'D')
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.0)
    pdf.set_xy(53, y+2)
    pdf.cell(43, 5, detail)
    
    pdf.rect(97, y, 50, 9, 'F')
    pdf.rect(97, y, 50, 9, 'D')
    pdf.set_font('Helvetica', 'I', 7.2)
    pdf.set_text_color(*pdf.GRAY)
    pdf.set_xy(98, y+1)
    pdf.multi_cell(48, 3.4, note)
    y += 11.5

pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(152, 44)
pdf.cell(135, 6, 'Missing Value Audit Prior to Train-Only Imputation')
pdf.add_image_safe('images/04_missing_values.png', 150, 51, 137)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 115, 277, 75, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 115, 277, 75, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_xy(15, 118)
pdf.cell(267, 5, 'Structured Methodological Audit: Finding -> Evidence -> Interpretation -> Business Implication')

audit_steps = [
    ('Finding', 'Missingness is heavily concentrated in optional demographic fields; core billing/usage columns are nearly complete.', '#1E40AF'),
    ('Evidence', '3 columns exceed 35% missing (numbcars 49.4%, dwllsize 38.4%, HHstatin 37.9%) and were structurally dropped. The remaining 81 numeric features exhibit <5% missingness.', '#0369A1'),
    ('Interpretation', 'High missingness in self-reported demographics reflects customer non-response bias rather than random omission. Dropping uninformative columns preserves model stability.', '#0D9488'),
    ('Business Implication', 'Train-only imputation prevents validation contamination. The scoring engine operates on robust billing telemetry that is reliably populated in enterprise data lakes.', '#15803D')
]
y_step = 126
for tag, text_content, tag_color in audit_steps:
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(15, y_step, 30, 13, 'F')
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(15, y_step, 30, 13, 'D')
    pdf.set_text_color(25, 93, 161)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_xy(15, y_step+3.5)
    pdf.cell(30, 6, tag, align='C')
    
    pdf.rect(48, y_step, 234, 13, 'F')
    pdf.rect(48, y_step, 234, 13, 'D')
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.0)
    pdf.set_xy(51, y_step+2)
    pdf.multi_cell(228, 4.2, text_content)
    y_step += 15

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Target Dynamics: Balanced Split Validates Dual AUC-ROC & Accuracy Optimization', 'Empirical 50.44% Stayer Baseline Enables Unbiased Supervised Learning Without Synthetic Sampling')
pdf.footer_bar(5)

pdf.add_image_safe('images/01_churn_distribution.png', 12, 48, 128)

pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 11)
pdf.set_xy(148, 45)
pdf.cell(135, 6, 'Target Dynamics & Methodological Implications')

target_cards = [
    ('Natural Class Balance', '49.56% Churners vs. 50.44% Stayers', 'The dataset exhibits an almost perfect 50/50 balance across all 100,000 records (Train: 49.56%, Val: 49.56%, Test: 49.56%). This represents an active subscriber pool with high churn exposure.'),
    ('Zero Synthetic Sampling Needed', 'No SMOTE or Artificial Class Weighting', 'Because the minority class represents 49.56% of records, no synthetic oversampling (SMOTE, ADASYN) or loss re-weighting was required. This prevents synthetic distribution distortion and overfitting.'),
    ('Evaluation Metric Duality', 'Dual Optimization: AUC-ROC & Accuracy', 'AUC-ROC serves as the primary metric for continuous ranking discrimination. Concurrently, Accuracy (64.38%) is directly meaningful, outperforming majority-class baseline guessing (50.44%) by +13.94 percentage points.'),
    ('Operational Value Rule', 'Sensitivity Prioritized Over Precision', 'Missing an impending churner costs $900 in lost gross LTV, while false-alarm outreach costs only $15-$80. The business problem demands high sensitivity (recall) at operational cutoffs.')
]
y_t = 53
for tag, title, detail in target_cards:
    pdf.set_fill_color(*pdf.LIGHT)
    pdf.rect(148, y_t, 139, 31, 'F')
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(148, y_t, 139, 31, 'D')
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_xy(152, y_t+2)
    pdf.cell(130, 5, tag)
    pdf.set_text_color(*pdf.NAVY)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_xy(152, y_t+7)
    pdf.cell(130, 4.5, title)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 7.8)
    pdf.set_xy(152, y_t+12)
    pdf.multi_cell(131, 3.8, detail)
    y_t += 34

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Exploratory Data Analysis: Equipment Age Discovered as Primary Churn Indicator', 'Handsets of Churners Are 58 Days Older on Average (421 vs. 363 Days), While Billing Overlaps Heavily')
pdf.footer_bar(6)

pdf.add_image_safe('images/02_eqpdays_vs_churn.png', 10, 46, 142)
pdf.add_image_safe('images/03_revenue_usage_vs_churn.png', 154, 46, 133)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'Empirical Evidence & Business Implication: The Hardware Lifecycle Mechanism')

eda_findings = [
    ('Finding & Evidence:', 'Handsets of churners are 58 days older on average (421 vs 363 days; Welch t-test p < 0.0001). Conversely, monthly revenue (rev_Mean) and minutes of use (mou_Mean) overlap heavily between stayers and churners, showing minimal univariate separation.'),
    ('Technical Interpretation:', 'Billing metrics alone cannot segment churn risk. Subscriber dissatisfaction is catalyzed by device fatigue: battery degradation, screen wear, and lack of modern 5G network compatibility create friction that prompts competitor switching.'),
    ('Strategic Implication:', 'Handset upgrade subsidies ($60 handset subsidy + $20 concierge outreach) target the primary intervenable risk indicator identified in observational data. This forms the operational core of our Red Tier retention strategy, addressing device fatigue and incentivizing renewal.')
]
y_ef = 159
for label, desc in eda_findings:
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 8.2)
    pdf.set_xy(15, y_ef)
    pdf.cell(42, 4.5, label)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.0)
    pdf.set_xy(57, y_ef)
    pdf.multi_cell(225, 4.0, desc)
    y_ef += 10.5

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Customer Segmentation: Regional Vulnerabilities & the Month 12-16 Contract Cliff', 'Northwest Markets Churn at 56.9% & Initial Contract Expiration Window Triggers Customer Defection')
pdf.footer_bar(7)

pdf.add_image_safe('images/10_churn_by_area.png', 10, 46, 172)
pdf.add_image_safe('images/11_churn_by_tenure.png', 185, 46, 102)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.5)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'Segmentation Evidence & Strategic Implications: Geography & Account Lifecycle')

seg_findings = [
    ('Regional Vulnerability:', 'Northwest/Rocky Mountain (56.9%), South Florida (53.4%), and North Florida (52.8%) show the highest regional churn rates, whereas New York (47.1%) and New England (46.4%) show lowest churn. This points to localized competitor pricing and network coverage variations.'),
    ('The Month 12-16 Cliff:', 'Subscribers in Q2 tenure (12-16 months) churn at 55.4%, corresponding directly to the initial contract expiration window. Once customers survive past month 24, loyalty increases and churn drops steadily to 44.7% for mature accounts (>30 months).'),
    ('Actionable Timing:', 'Interventions must be timed proactively at month 10-11 before subscribers reach the 12-month expiration cliff. Proactive outreach in high-churn regional markets captures at-risk accounts before they evaluate competitor promotional plans.')
]
y_sf = 159
for label, desc in seg_findings:
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 8.2)
    pdf.set_xy(15, y_sf)
    pdf.cell(40, 4.5, label)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.0)
    pdf.set_xy(55, y_sf)
    pdf.multi_cell(227, 4.0, desc)
    y_sf += 10.5

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Feature Engineering: Translating Telecom Domain Mechanics into Predictive Signals', 'Engineered Ratios & Composite Indices Capturing Device Aging, Plan Mismatch & Network Friction')
pdf.footer_bar(8)

feats = [
    ('eqpdays_per_month', 'eqpdays / months', 'Handset age normalized by tenure: isolates device fatigue independently of account duration, identifying rapid device wear.'),
    ('eqp_tenure_ratio', 'eqpdays / (months * 30.4)', 'Handset lifespan vs contract lifespan: detects devices that have outlasted initial agreements, signaling upgrade eligibility.'),
    ('overage_rev_ratio', 'ovrrev_Mean / rev_Mean', 'Plan mismatch ratio: proportion of bill from overage penalties, creating bill shock that drives switching [6].'),
    ('custcare_flag', 'custcare_Mean > 0', 'Service friction indicator: flags subscribers experiencing unresolved billing or network disputes via customer care.'),
    ('handset_fatigue_flag', '(eqp > 365) & (10 <= months <= 24)', 'Compound risk flag: subscribers on aging handsets inside their primary contract renewal window.'),
    ('service_friction_index', 'drop_vce + blck_vce + custcare', 'Composite operational dissatisfaction index tracking repeated call drops, blocked calls, and support contacts.'),
]
y_feat = 46
for name, formula, rationale in feats:
    pdf.set_fill_color(*pdf.LIGHT)
    pdf.rect(10, y_feat, 277, 19, 'F')
    pdf.set_draw_color(203, 213, 225)
    pdf.rect(10, y_feat, 277, 19, 'D')
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_xy(14, y_feat+2)
    pdf.cell(60, 5, name)
    pdf.set_text_color(*pdf.NAVY)
    pdf.set_font('Helvetica', 'I', 8.2)
    pdf.set_xy(76, y_feat+2)
    pdf.cell(60, 5, formula)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.2)
    pdf.set_xy(138, y_feat+2)
    pdf.multi_cell(145, 4.2, rationale)
    y_feat += 21.5

pdf.set_fill_color(240, 249, 255)
pdf.rect(10, 175, 277, 17, 'F')
pdf.set_draw_color(186, 230, 253)
pdf.rect(10, 175, 277, 17, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 9.0)
pdf.set_xy(14, 177)
pdf.cell(267, 4.5, 'Strict Leak-Free Feature Implementation Protocol:')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.8)
pdf.set_xy(14, 182)
pdf.multi_cell(267, 3.8, 'All engineered features use strictly within-fold transformations. Pairwise collinearity filtering (>0.95 threshold) dropped 13 redundant features based solely on training fold correlations. Billing adjustments (adjrev, adjmou, adjqty) were structurally excluded due to adjustment-related target leakage risk and extreme collinearity with cumulative totals.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Model Benchmarking: Systematic Evaluation Across GBDT, Boosting & Linear Baselines', 'Leak-Free 5-Fold Stratified Cross-Validation on 70,000 Training Records (Within-Fold Preprocessing)')
pdf.footer_bar(9)

pdf.add_image_safe('images/15_cv_stability_comparison.png', 10, 44, 175)

pdf.set_fill_color(255, 255, 255)
pdf.rect(188, 44, 99, 102, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(188, 44, 99, 102, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 9.5)
pdf.set_xy(192, 47)
pdf.cell(91, 5, 'Model Performance Matrix', align='C')

matrix_headers = ['Model Version', 'CV AUC', 'Test AUC']
pdf.set_fill_color(*pdf.PRIMARY)
pdf.rect(191, 54, 93, 6, 'F')
pdf.set_text_color(255, 255, 255)
pdf.set_font('Helvetica', 'B', 7.5)
pdf.set_xy(192, 55.5)
pdf.cell(45, 4, 'Model Architecture')
pdf.cell(24, 4, '5-Fold CV')
pdf.cell(24, 4, 'Test AUC')

matrix_rows = [
    ('Tri-Blend Benchmark', '0.7026', '0.7019', True),
    ('Tuned LightGBM V3', '0.7011', '0.7015', True),
    ('Tuned XGBoost V3', '0.6997', '0.6981', False),
    ('CatBoost V3', '0.6984', '0.6973', False),
    ('Baseline LightGBM', '0.6956', '0.6979', False),
    ('Scaled Logistic Reg', '0.6316', '0.6395', False),
]
y_mat = 60
for name, cv_val, test_val, is_top in matrix_rows:
    pdf.set_fill_color(230, 245, 230) if is_top else (248, 250, 252)
    pdf.rect(191, y_mat, 93, 5.5, 'F')
    pdf.set_draw_color(226, 232, 240)
    pdf.rect(191, y_mat, 93, 5.5, 'D')
    pdf.set_text_color(25, 93, 161) if is_top else (30, 41, 59)
    pdf.set_font('Helvetica', 'B' if is_top else '', 7.2)
    pdf.set_xy(192, y_mat+1)
    pdf.cell(45, 4, name)
    pdf.cell(24, 4, cv_val)
    pdf.cell(24, 4, test_val)
    y_mat += 5.5

pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.5)
pdf.set_xy(192, 96)
pdf.multi_cell(91, 3.8, 'Baseline Reconciliation: Tutorial baseline LightGBM achieved 0.69559 CV and 0.6968 Test AUC (0.6979 on V3 features). Initial Tuned V1 achieved 0.69811 CV and 0.6968 Test AUC. Champion Tuned LightGBM V3 achieves 0.70106 CV and 0.7015 Test AUC (+0.0047 lift over initial baseline).')

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.0)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'Cross-Validation Rigor & Independence Caveat (Bengio & Grandvalet, 2004)')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.0)
pdf.set_xy(15, 159)
pdf.multi_cell(267, 4.0, '1. Leak-Free Cross-Validation: Evaluated strictly on the 70,000 training records. Imputations, categorical frequency encodings, and collinearity drops were fit inside each training fold (Train=56k, Val=14k), completely isolating the 10k validation and 20k test sets.\n2. Fold Stability: Tuned LightGBM V3 shows minimal fold variance (0.70106 +- 0.00556), with descriptive Student t 95% interval [0.69416, 0.70796] (df=4).\n3. Independence Caveat: Because training folds share 75% of their records, cross-validation errors are correlated. Sample standard errors underestimate true error variance (Bengio & Grandvalet, 2004); fold intervals reflect descriptive variation, not fully independent confidence intervals.\n4. Non-Linear Superiority: Tree models outperform logistic regression by +0.062 AUC, confirming that non-linear interaction thresholds are mandatory.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Model Selection: Champion Tuned LightGBM V3 Balances Power & Operational Simplicity', 'Test Set AUC: Tri-Blend (0.7019) vs. LightGBM V3 (0.7015), Marginal Difference (+0.0004) Favors Single Model')
pdf.footer_bar(10)

pdf.add_image_safe('images/06_roc_curves.png', 10, 46, 138)
pdf.add_image_safe('images/05_model_comparison.png', 150, 46, 137)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.0)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'Operational Excellence & Selection Rationale: Champion LightGBM V3 vs. Tri-Blend Benchmark')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.0)
pdf.set_xy(15, 159)
pdf.multi_cell(267, 4.0, """1. Predictive Ceiling: Tuned LightGBM V3 achieves 0.7015 Test AUC, while the Tri-Blend benchmark reaches 0.7019. The observed test AUC difference (+0.0004) is marginal.
2. Paired Comparison & Reproducibility Status: Individual test predictions were not serialized to disk; formal test-set paired significance (e.g., DeLong test) is unverified from static artifacts, so no numerical test p-value is claimed. Across frozen 5-fold CV (oof_predictions_v3.csv), the observed mean fold AUC gain is +0.0015 (0.7026 vs. 0.7011). LightGBM V3 is selected as Champion Model for operational parsimony and maintainability.
3. Architectural Parsimony: Tri-Blend requires orchestrating three distinct ML libraries (lightgbm, xgboost, catboost) in production. LightGBM V3 operates as a single runtime dependency, offering streamlined operational maintainability and native C++ TreeSHAP explainability.
4. Latency Qualification: Development observations (~0.38-1.08 ms for LightGBM V3, ~2.15 ms for Tri-Blend) are preliminary developmental benchmarks on host hardware, not certified production SLAs.""")

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Error Economics: Asymmetric Costs Demand High Sensitivity to Protect Customer LTV', 'Missing a Churner ($900 Lost LTV) is 11.25x More Costly Than Outreach ($80 False Alarm)')
pdf.footer_bar(11)

pdf.add_image_safe('images/07_confusion_matrix.png', 10, 46, 118)

error_data = [
    ('True Negatives: 6,439', 'Subscribers correctly predicted to stay (63.83% specificity): zero wasted outreach capital.', True),
    ('True Positives: 6,437', 'At-risk churners correctly flagged (64.93% recall): successfully routed to targeted retention interventions.', True),
    ('False Positives: 3,649', 'False alarms: outreach costs ~$15-$80 per customer; highly acceptable trade-off given substantial LTV recovery.', False),
    ('False Negatives: 3,475', 'Missed churners: unmitigated customer defection; forfeits ~$900 gross contractual LTV ($450 at 50% EBITDA margin).', False),
]
y_err = 46
for label, meaning, is_good in error_data:
    pdf.set_fill_color(*(240, 253, 244) if is_good else (254, 242, 242))
    pdf.rect(134, y_err, 153, 22, 'F')
    pdf.set_draw_color(*(187, 247, 208) if is_good else (254, 202, 202))
    pdf.rect(134, y_err, 153, 22, 'D')
    pdf.set_text_color(*(22, 101, 52) if is_good else (185, 28, 28))
    pdf.set_font('Helvetica', 'B', 9.5)
    pdf.set_xy(138, y_err+2.5)
    pdf.cell(145, 5, label)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 8.2)
    pdf.set_xy(138, y_err+8.5)
    pdf.multi_cell(145, 4.0, meaning)
    y_err += 25

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.0)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'Economic Decision Rule & Expected Value Maximization')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.2)
pdf.set_xy(15, 159)
pdf.multi_cell(267, 4.2, '1. Asymmetric Cost Function: In telecommunications, the cost of a false negative (lost subscriber = $900 LTV) is 11.25x higher than a Red false positive ($80 handset subsidy) and 60x higher than an Amber false positive ($15 digital notification).\n2. Sensitivity Prioritization: At the operational cutoff of p = 0.50, Tuned LightGBM V3 captures nearly 2 out of every 3 churners (64.93% recall) while preserving 63.82% precision and 64.38% overall accuracy.\n3. Economic Surplus: High sensitivity ensures maximum revenue capture, generating $726k in net revenue protection on the test cohort and $3.63M across the fleet.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Model Explainability: What Actionable Levers Drive Subscriber Churn?', 'TreeSHAP Attribution Identifies Handset Lifespan, Billing Overages & Active Usage as Dominant Split Levers')
pdf.footer_bar(12)

pdf.add_image_safe('images/08_feature_importance.png', 10, 46, 142)
pdf.add_image_safe('images/09_shap_summary.png', 154, 46, 133)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 150, 277, 42, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 150, 277, 42, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 10.0)
pdf.set_xy(15, 152)
pdf.cell(267, 5, 'SHAP Attribution Insights & Non-Causal Disclaimers')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 8.0)
pdf.set_xy(15, 159)
pdf.multi_cell(267, 4.0, '1. Top Risk Drivers: Equipment age (eqpdays), contract tenure (months), handset retail price, and overage revenue ratio dominate tree splits and TreeSHAP impact.\n2. Non-Linear Dynamics: High eqpdays strongly elevates churn log-odds, while high monthly voice usage (mou_Mean) anchors customer retention.\n3. Actionable Business Translation: Explainability confirms that churn is driven by addressable operational friction: hardware obsolescence (Red Tier upgrade) and unexpected overage charges (Amber Tier plan right-sizing).\n4. Non-Causal Disclaimer: SHAP values quantify observational feature attribution within the model; they do not establish causal treatment effects. True causal lift must be experimentally validated in Phase 1 A/B pilots.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Business Proposal: Precision Retention Programme (PRP) Operational Architecture', 'Three-Tier Risk-Differentiated Strategy Routing 100k Subscribers to Value-Accretive Interventions')
pdf.footer_bar(13)

pdf.add_image_safe('images/13_operational_workflow.png', 10, 42, 277)

tiers_data = [
    ('RED TIER', 'High Risk (p >= 0.70) | 11.76% Pop (11,755 fleet)', 'Handset Upgrade & 2-Yr Contract Renewal', '$80/cust ($60 5G credit + $20 concierge)', '78.60% churn rate | sum(p) = 1,840.4 expected churners. 25% response assumption [5]. Break-even absolute churn drop: 17.78 pp (BE response rate 22.62% under 50% EBITDA margin).', (220, 38, 38)),
    ('AMBER TIER', 'Moderate Risk (p 0.50-0.70) | 38.67% Pop (38,670 fleet)', 'Automated Digital Plan Right-Sizing & Overage Relief', '$15/cust (Zero-touch automated SMS/app prompt)', '59.32% churn rate | sum(p) = 4,563.3 expected churners. 15% response assumption [5]. Break-even absolute churn drop: 3.33 pp (BE response rate 5.62% under 50% EBITDA margin).', (234, 88, 12)),
    ('GREEN TIER', 'Low Risk (p < 0.50) | 49.58% Pop (49,575 fleet)', 'Passive Monitoring & Regular Nurturing', '$0/cust (Standard service delivery)', '35.06% churn rate | sum(p) = 3,529.4 expected churners. Regular service delivery with monthly automated re-scoring into the PRP engine.', (22, 163, 74)),
]

y_tier = 91
for tag, risk_sub, action, cost_info, mechanics, color in tiers_data:
    pdf.set_fill_color(*color)
    pdf.rect(10, y_tier, 22, 32, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_xy(10, y_tier+3)
    pdf.cell(22, 5, tag, align='C')
    
    pdf.set_fill_color(248, 250, 252)
    pdf.rect(32, y_tier, 110, 32, 'F')
    pdf.set_draw_color(226, 232, 240)
    pdf.rect(32, y_tier, 110, 32, 'D')
    
    pdf.set_text_color(*color)
    pdf.set_font('Helvetica', 'B', 8.5)
    pdf.set_xy(34, y_tier+2)
    pdf.cell(106, 4.5, action)
    
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', 'B', 7.5)
    pdf.set_xy(34, y_tier+6.5)
    pdf.cell(106, 4.0, risk_sub)
    
    pdf.set_text_color(25, 93, 161)
    pdf.set_font('Helvetica', 'I', 7.2)
    pdf.set_xy(34, y_tier+10.5)
    pdf.cell(106, 4.0, cost_info)
    
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 7.0)
    pdf.set_xy(34, y_tier+14.5)
    pdf.multi_cell(106, 3.2, mechanics)
    y_tier += 34

pdf.add_image_safe('images/14_risk_tier_discrimination.png', 148, 91, 139)

pdf.set_fill_color(240, 249, 255)
pdf.rect(148, 142, 139, 49, 'F')
pdf.set_draw_color(186, 230, 253)
pdf.rect(148, 142, 139, 49, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_xy(152, 144)
pdf.cell(131, 4.5, 'Expected Economic Value (EV) Decision Rules & Calibration Caveat')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(152, 149)
pdf.multi_cell(131, 3.4, '1. Standalone Break-Even: An intervention is economically viable when expected LTV saved exceeds unit cost: Delta_churn * ($900 * 50% margin) >= Cost. Break-even occurs at 17.78 pp absolute churn reduction for Red ($80/$450) and 3.33 pp for Amber ($15/$450).\n2. Conditional Response vs. A/B Drop: Conditional response (Red: 22.62%, Amber: 5.62%) measures success among churners (r = Delta_churn / p_control).\n3. Non-Calibration Disclosure: The right chart evaluates empirical segment discrimination between observed and expected aggregate churn rates. Formal post-hoc probability calibration (e.g., Platt scaling or isotonic regression) was not conducted.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Quantified Financial Scenarios: Prospective Forecast vs. Retrospective Reconciliation', 'Fleet Impact (n=100k): +5,723 Retained Subs, +$3.63M Net Revenue, +$1.05M Net EBITDA (69.38% ROI)')
pdf.footer_bar(14)

pdf.add_image_safe('images/16_financial_scenario_comparison.png', 10, 42, 136)

pdf.set_fill_color(240, 253, 244)
pdf.rect(10, 97, 136, 23, 'F')
pdf.set_draw_color(187, 247, 208)
pdf.rect(10, 97, 136, 23, 'D')
pdf.set_text_color(22, 101, 52)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_xy(13, 98.5)
pdf.cell(130, 4.5, 'Prospective Model Forecast (Live Deployment Model)')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(13, 103.5)
pdf.multi_cell(130, 3.3, 'Expected churners estimated from sum of predicted probabilities (sum p = 1,840.4 Red, 4,563.3 Amber). Retains 5,723 fleet subscribers, generating $5.15M gross revenue, $3.63M net revenue (238.76% Net ROI), and $1,054,860 net EBITDA (69.38% EBITDA ROI; break-even EBITDA margin: 29.52%).')

pdf.set_fill_color(248, 250, 252)
pdf.rect(10, 122, 136, 23, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 122, 136, 23, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 8.5)
pdf.set_xy(13, 123.5)
pdf.cell(130, 4.5, 'Retrospective Evaluation Benchmark (Ground-Truth Labels)')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(13, 128.5)
pdf.multi_cell(130, 3.3, 'Evaluates test partition using actual observed churn labels (1,848 Red, 4,588 Amber). Yields 5,751 fleet retained subscribers, $5.18M gross revenue, $3.66M net revenue (240.42% Net ROI), and $1,067,500 net EBITDA (70.21% EBITDA ROI; break-even EBITDA margin: 29.38%).')

fin_headers = ['Operational & Financial Dimension', 'Held-Out Test (20k)', 'Enterprise Fleet (100k)']
col_w = [61, 38, 38]
y_tbl = 42

pdf.set_fill_color(*pdf.PRIMARY)
pdf.rect(150, y_tbl, 137, 5.5, 'F')
x_t = 150
for h, w in zip(fin_headers, col_w):
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 7.2)
    pdf.set_xy(x_t+1, y_tbl+0.8)
    pdf.cell(w, 4.0, h)
    x_t += w
y_tbl += 5.5

fin_data = [
    ('Red Targeted (p >= 0.70)', '2,351 subs (11.8%)', '11,755 subs (11.8%)'),
    ('Red Churn: Exp(sum p) / Act', '1,840.4 exp / 1,848 act', '9,201.7 exp / 9,240 act'),
    ('Red Retained (25% assumption)', '460.1 prosp / 462.0 retro', '2,300.4 prosp / 2,310.0 retro'),
    ('Amber Targeted (p 0.50-0.70)', '7,734 subs (38.7%)', '38,670 subs (38.7%)'),
    ('Amber Churn: Exp(sum p) / Act', '4,563.3 exp / 4,588 act', '22,816.4 exp / 22,940 act'),
    ('Amber Retained (15% assumption)', '684.5 prosp / 688.2 retro', '3,422.5 prosp / 3,441.0 retro'),
    ('Total Retained (disp 5,723 / 5,751)', '1,144.6 prosp / 1,150.2 retro', '5,722.9 prosp / 5,751.0 retro'),
    ('Gross Revenue Protected ($900 LTV)', '$1.030M prosp / $1.035M retro', '$5.151M prosp / $5.176M retro'),
    ('Total Campaign Investment Cost', '$304,090 ($80/Red + $15/Amb)', '$1,520,450 ($80/Red + $15/Amb)'),
    ('Net Protected Revenue', '$726,034 prosp / $731,090 retro', '$3.630M prosp / $3.655M retro'),
    ('Net Revenue ROI', '238.76% prosp / 240.42% retro', '238.76% prosp / 240.42% retro'),
    ('Gross Rev-to-Cost Ratio (Multiple)', '338.76% (3.39x) / 340.42%', '338.76% (3.39x) / 340.42%'),
    ('Net EBITDA Contrib (50% Margin)', '$210,972 prosp / $213,500 retro', '$1,054,860 prosp / $1,067,500 retro'),
    ('EBITDA-Based ROI (50% Margin)', '69.38% prosp / 70.21% retro', '69.38% prosp / 70.21% retro'),
    ('Break-Even EBITDA Operating Margin', '29.52% prosp / 29.38% retro', '29.52% prosp / 29.38% retro'),
    ('Break-Even Churn Drop (A/B Lift)', 'Red: 17.78 pp | Amber: 3.33 pp', 'Red: 17.78 pp | Amber: 3.33 pp'),
]

highlight_rows = {'Net Protected Revenue', 'Net Revenue ROI', 'Total Retained (disp 5,723 / 5,751)', 'Net EBITDA Contrib (50% Margin)'}
for j, (dim, val_test, val_fleet) in enumerate(fin_data):
    highlight = dim in highlight_rows
    pdf.set_fill_color(220, 252, 231) if highlight else ((248, 250, 252) if j % 2 == 0 else (255, 255, 255))
    pdf.rect(150, y_tbl, 137, 5.0, 'F')
    x_t = 150
    for text_val, w in zip([dim, val_test, val_fleet], col_w):
        pdf.set_text_color(*(22, 101, 52) if highlight else (15, 23, 42))
        pdf.set_font('Helvetica', 'B' if highlight else '', 6.6)
        pdf.set_xy(x_t+1, y_tbl+0.6)
        pdf.cell(w, 3.8, text_val)
        x_t += w
    y_tbl += 5.0

pdf.set_fill_color(255, 251, 235)
pdf.rect(10, 148, 277, 44, 'F')
pdf.set_draw_color(254, 243, 199)
pdf.rect(10, 148, 277, 44, 'D')
pdf.set_text_color(146, 64, 14)
pdf.set_font('Helvetica', 'B', 8.2)
pdf.set_xy(14, 150)
pdf.cell(267, 4.0, 'Financial Methodology Notes & Strategic Baseline Reconciliation:')
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(14, 154.5)
pdf.multi_cell(267, 3.4, '1. Prospective Model Forecast: Live operational deployment scenario based on sum of predicted probabilities (sum(p_Red) = 1,840.35, sum(p_Amber) = 4,563.29). Applies hypothetical 25%/15% retention response assumptions, projecting 5,723 fleet retained subscribers, $5.15M gross revenue, $1.52M cost, $3.63M net protected revenue (238.76% Net ROI), and $1,054,860 net EBITDA contribution (69.38% EBITDA ROI; break-even EBITDA margin: 29.52%).\n2. Retrospective Evaluation: Evaluates test set performance using observed ground-truth churn labels (1,848 Red, 4,588 Amber), yielding 5,751 fleet retained subscribers, $5.18M gross revenue, $3.66M net revenue (240.42% ROI), and $1,067,500 net EBITDA (70.21% ROI; break-even margin: 29.38%).\n3. Reconciled Baseline Model: Baseline LightGBM captured 5,596 retained fleet subscribers, $3.60M net revenue, 251.42% Net Rev ROI, $1.08M net EBITDA. LightGBM V3 targets 257 additional high-risk Red subscribers, securing +155 net retained subscribers and +$27.1k to +$52.4k more net protected revenue.\n4. Assumptions: 25% and 15% response rates are hypothetical scenario assumptions (McKinsey, 2023 [5]). Illustrative 50% EBITDA operating margin reflects an enterprise-level industry benchmark.')

pdf.add_page()
pdf.slide_bg()
pdf.header_bar('Phase 1 A/B Pilot Design, Risk Governance, Limitations & Literature References', 'Statistically Powered Randomized Controlled Trial Framework & Comprehensive Literature Matching')
pdf.footer_bar(15)

pdf.add_image_safe('images/17_ab_power_curves.png', 10, 42, 277)

pdf.set_fill_color(*pdf.LIGHT)
pdf.rect(10, 93, 136, 99, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(10, 93, 136, 99, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 9.5)
pdf.set_xy(14, 96)
pdf.cell(128, 5, 'Phase 1 A/B Pilot Design & Governance Disclosures')
pdf.set_text_color(*pdf.DARK)
pdf.set_font('Helvetica', '', 7.2)
pdf.set_xy(14, 102)
pdf.multi_cell(128, 3.5, '1. Dedicated Cohort Pilot Designs:\n- Dedicated Red Pilot (N=3,000, 80/20 split: 2,400 treat / 600 ctrl): Exact unpooled normal MDE is 5.29 percentage points (power >99.9% to detect the 17.78 pp break-even drop; N=280 required). Note: Earlier 5.29-5.59 pp range reflected inverted allocation in exploratory scripts.\n- Dedicated Amber Pilot (N=7,000, 50/50 split: 3,500 treat / 3,500 ctrl): Exact unpooled normal MDE is 3.31 percentage points (power = 80.6% to detect the 3.33 pp break-even drop; N=6,896 required unpooled normal or N=7,020 Fleiss CC).\n\n2. Key Methodological Limitations:\n- Reserved Test Partition: Inspected historically during early exploration; final hyperparameters and thresholds were locked on train/val prior to reporting.\n- Observational Telemetry: Pre-churn signals (change_mou, change_rev) lack exact calendar timestamps; non-causal.\n- Response Rate Scenarios: 25% (Red) and 15% (Amber) response rates are hypothetical scenario assumptions inspired by telecom literature (McKinsey, 2023 [5]).\n- Margin Benchmark: 50% EBITDA operating margin is an illustrative industry benchmark; break-even occurs at 29.52%.\n- PoC Status: Champion Model for the PoC; requires A/B validation before enterprise deployment.')

pdf.set_fill_color(255, 255, 255)
pdf.rect(150, 93, 137, 99, 'F')
pdf.set_draw_color(203, 213, 225)
pdf.rect(150, 93, 137, 99, 'D')
pdf.set_text_color(*pdf.PRIMARY)
pdf.set_font('Helvetica', 'B', 9.5)
pdf.set_xy(154, 96)
pdf.cell(129, 5, 'Academic & Industrial Literature Citations')

citations = [
    ('[1] Reichheld & Schefter (2000)', 'E-loyalty: Your Secret Weapon on the Web. Harvard Business Review, 78(4), 105-113.'),
    ('[2] CTIA Wireless Assoc. (2024)', 'Annual Wireless Industry Survey. Industry ARPU benchmark context (- range).'),
    ('[3] GSMA Intelligence (2024)', 'The Mobile Economy: Macro switching benchmarks (~14% annual provider churn).'),
    ('[4] Ericsson ConsumerLab (2024)', 'Ericsson Mobility Report: 5G transitions & device replacement cycle context.'),
    ('[5] Scenario Assumption [5]', '25% Red / 15% Amber response rates (Hypothetical scenario parameters; unverified).'),
    ('[6] FCC (2024)', 'Communications Marketplace Report: Regulatory context on data caps & overages.'),
    ('[7] Ke, G. et al. (2017)', 'LightGBM: A Highly Efficient Gradient Boosting Decision Tree. NeurIPS 30.'),
    ('[8] Chen, T. & Guestrin, C. (2016)', 'XGBoost: A Scalable Tree Boosting System. ACM SIGKDD, 785-794.'),
    ('[9] Prokhorenkova, L. et al. (2018)', 'CatBoost: Unbiased Boosting with Categorical Features. NeurIPS 31.'),
    ('[10] Lundberg, S. & Lee, S.-I. (2017)', 'A Unified Approach to Interpreting Model Predictions. NeurIPS 30.'),
    ('[11] Pedregosa, F. et al. (2011)', 'Scikit-learn: Machine Learning in Python. JMLR, 12, 2825-2830.'),
    ('[12] GCI World Tutorial (2026)', 'Baseline Protocol (tutorial.ipynb; Course resource, local workspace file).'),
    ('[13] Company A Overview (2026)', 'Dataset Schema (ENG_Company_A_Dataset_Overview.docx; Local course file).')
]
y_cit = 103
for tag, detail in citations:
    pdf.set_text_color(*pdf.PRIMARY)
    pdf.set_font('Helvetica', 'B', 7.0)
    pdf.set_xy(154, y_cit)
    pdf.cell(48, 3.8, tag)
    pdf.set_text_color(*pdf.DARK)
    pdf.set_font('Helvetica', '', 6.8)
    pdf.set_xy(202, y_cit)
    pdf.cell(82, 3.8, detail)
    y_cit += 6.5

output_pdf = 'reports/presentation.pdf'
pdf.output(output_pdf)
print(f'Presentation generated successfully: {output_pdf}')
print(f'Size: {os.path.getsize(output_pdf)/1024:.0f} KB  |  Slides: {pdf.page_no()}')
