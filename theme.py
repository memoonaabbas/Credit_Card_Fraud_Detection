"""
theme.py
----------------------------------------------------------------------
Shared visual theme for the Credit Card Fraud Detection app.

This module contains ONLY presentation code (CSS + small UI helpers).
It does not touch any ML / data logic, so it is safe to import from
every page without affecting model loading, scaling or predictions.
----------------------------------------------------------------------
"""

import streamlit as st

# ============================================================
# Design Tokens
# ============================================================

NAVY = "#0B3C6D"        # Primary — headings, primary actions
DEEP_NAVY = "#082A4D"
STEEL = "#1B6FA8"        # Secondary accent — links, highlights
GOLD = "#C9962B"        # Premium accent — card stripe, dividers
BG = "#EAF4FF"        # App background
CARD = "#FFFFFF"
BORDER = "#D9E6F5"
MUTED = "#5B6B82"
SUCCESS = "#178A54"
SUCCESS_BG = "#EAF9F1"
DANGER = "#C23B3B"
DANGER_BG = "#FDEDEC"


def inject_base_css():
    """Injects the global stylesheet shared by every page."""
    st.markdown(
        f"""
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700;800&family=Inter:wght@400;500;600&display=swap');

        html, body, [class*="css"] {{
            font-family: 'Inter', sans-serif;
        }}

        h1, h2, h3, h4, h5 {{
            font-family: 'Poppins', sans-serif;
            color: {NAVY};
            letter-spacing: -0.01em;
        }}

        /* ---------------- App shell ---------------- */
        [data-testid="stAppViewContainer"] {{
            background: {BG};
        }}

        [data-testid="stHeader"] {{
            background: transparent;
            visibility: hidden;
            height: 0;
        }}

        .block-container {{
            padding-top: 2rem;
            padding-bottom: 3rem;
            max-width: 1200px;
        }}

        /* ---------------- Sidebar ---------------- */
        [data-testid="stSidebar"] {{
            background: {CARD};
            border-right: 1px solid {BORDER};
        }}

        [data-testid="stSidebar"] > div:first-child {{
            padding-top: 0.5rem;
        }}

        /* Streamlit's auto page-navigation, styled to look like a premium menu */
        [data-testid="stSidebarNav"] {{
            padding: 0.75rem 0.5rem 0.5rem 0.5rem;
            border-bottom: 1px solid {BORDER};
            margin-bottom: 0.75rem;
        }}

        [data-testid="stSidebarNav"] a {{
            border-radius: 10px;
            padding: 0.5rem 0.75rem;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
            color: {NAVY} !important;
            transition: 0.2s;
        }}

        [data-testid="stSidebarNav"] a:hover {{
            background: {BG};
        }}

        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background: linear-gradient(90deg, {NAVY}, {STEEL});
            color: white !important;
            box-shadow: 0 4px 10px rgba(11,60,109,0.25);
        }}

        [data-testid="stSidebarNav"] a[aria-current="page"] span {{
            color: white !important;
        }}

        .sidebar-brand {{
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 0.25rem 0.25rem 1rem 0.25rem;
        }}

        .sidebar-brand .icon {{
            font-size: 28px;
        }}

        .sidebar-brand .title {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 17px;
            color: {NAVY};
            line-height: 1.15;
        }}

        .sidebar-brand .subtitle {{
            font-size: 11.5px;
            color: {MUTED};
            font-weight: 500;
        }}

        .sidebar-badge {{
            background: {BG};
            border: 1px solid {BORDER};
            border-radius: 12px;
            padding: 12px 14px;
            margin-bottom: 10px;
        }}

        .sidebar-badge .label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: {MUTED};
            font-weight: 600;
            margin-bottom: 4px;
        }}

        .sidebar-badge .value {{
            font-size: 14.5px;
            font-weight: 600;
            color: {NAVY};
        }}

        .sidebar-dev-card {{
            background: linear-gradient(160deg, {NAVY}, {DEEP_NAVY});
            border-radius: 14px;
            padding: 16px;
            color: white;
            margin-top: 4px;
        }}

        .sidebar-dev-card .name {{
            font-family: 'Poppins', sans-serif;
            font-weight: 600;
            font-size: 15px;
        }}

        .sidebar-dev-card .role {{
            font-size: 12px;
            opacity: 0.8;
            margin-top: 2px;
        }}

        /* ---------------- Cards ---------------- */
        .premium-card {{
            background: {CARD};
            border-radius: 18px;
            padding: 28px 30px;
            box-shadow: 0 10px 28px rgba(11,60,109,0.08);
            border-top: 4px solid;
            border-image: linear-gradient(90deg, {NAVY}, {GOLD}) 1;
            margin-bottom: 22px;
        }}

        .plain-card {{
            background: {CARD};
            border-radius: 18px;
            padding: 26px 28px;
            box-shadow: 0 8px 22px rgba(11,60,109,0.07);
            margin-bottom: 20px;
        }}

        .hero-card {{
            background: linear-gradient(120deg, {NAVY} 0%, {STEEL} 100%);
            border-radius: 22px;
            padding: 46px 40px;
            color: white;
            box-shadow: 0 16px 34px rgba(11,60,109,0.28);
            margin-bottom: 26px;
            position: relative;
            overflow: hidden;
        }}

        .hero-card::after {{
            content: "";
            position: absolute;
            right: -60px;
            top: -60px;
            width: 220px;
            height: 220px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(201,150,43,0.35), transparent 70%);
        }}

        .hero-card h1 {{
            color: white;
            font-size: 2.3rem;
            margin-bottom: 10px;
        }}

        .hero-card p {{
            color: rgba(255,255,255,0.88);
            font-size: 15.5px;
            max-width: 640px;
            line-height: 1.55;
        }}

        .eyebrow {{
            display: inline-block;
            background: rgba(201,150,43,0.18);
            color: {GOLD};
            font-weight: 600;
            font-size: 12px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 5px 12px;
            border-radius: 999px;
            margin-bottom: 14px;
        }}

        .eyebrow-light {{
            display: inline-block;
            background: rgba(255,255,255,0.15);
            color: white;
            font-weight: 600;
            font-size: 12px;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            padding: 5px 12px;
            border-radius: 999px;
            margin-bottom: 14px;
        }}

        /* ---------------- Metric tiles ---------------- */
        .metric-tile {{
            background: {CARD};
            border-radius: 16px;
            padding: 20px 18px;
            text-align: left;
            box-shadow: 0 8px 20px rgba(11,60,109,0.07);
            border: 1px solid {BORDER};
            transition: 0.25s;
            height: 100%;
        }}

        .metric-tile:hover {{
            transform: translateY(-4px);
            box-shadow: 0 14px 26px rgba(11,60,109,0.14);
        }}

        .metric-tile .icon {{
            font-size: 22px;
            margin-bottom: 6px;
        }}

        .metric-tile .value {{
            font-family: 'Poppins', sans-serif;
            font-size: 1.7rem;
            font-weight: 700;
            color: {NAVY};
            line-height: 1.1;
        }}

        .metric-tile .label {{
            font-size: 12.5px;
            color: {MUTED};
            font-weight: 500;
            margin-top: 4px;
        }}

        /* ---------------- Feature cards ---------------- */
        .feature-card {{
            background: {CARD};
            border-radius: 16px;
            padding: 24px;
            box-shadow: 0 8px 20px rgba(11,60,109,0.07);
            border: 1px solid {BORDER};
            transition: 0.25s;
            height: 100%;
        }}

        .feature-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 14px 26px rgba(11,60,109,0.14);
            border-color: {STEEL};
        }}

        .feature-card .f-icon {{
            font-size: 26px;
            margin-bottom: 8px;
        }}

        .feature-card h4 {{
            margin: 0 0 6px 0;
            font-size: 16px;
        }}

        .feature-card p {{
            color: {MUTED};
            font-size: 13.5px;
            margin: 0;
            line-height: 1.5;
        }}

        /* ---------------- Result banners ---------------- */
        .result-safe {{
            background: {SUCCESS_BG};
            border: 1.5px solid {SUCCESS};
            border-radius: 16px;
            padding: 22px 26px;
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
        }}

        .result-fraud {{
            background: {DANGER_BG};
            border: 1.5px solid {DANGER};
            border-radius: 16px;
            padding: 22px 26px;
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 16px;
        }}

        .result-icon {{
            font-size: 34px;
        }}

        .result-title {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 17px;
        }}

        .result-safe .result-title {{ color: {SUCCESS}; }}
        .result-fraud .result-title {{ color: {DANGER}; }}

        .result-sub {{
            font-size: 13px;
            color: {MUTED};
            margin-top: 2px;
        }}

        /* ---------------- Workflow steps ---------------- */
        .step-row {{
            display: flex;
            align-items: center;
            gap: 14px;
            padding: 10px 4px;
        }}

        .step-num {{
            min-width: 34px;
            height: 34px;
            border-radius: 50%;
            background: linear-gradient(135deg, {NAVY}, {STEEL});
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-family: 'Poppins', sans-serif;
            font-size: 13.5px;
        }}

        .step-label {{
            font-weight: 600;
            color: {NAVY};
            font-size: 14.5px;
        }}

        .step-connector {{
            width: 2px;
            height: 16px;
            background: {BORDER};
            margin-left: 17px;
        }}

        /* ---------------- Buttons ---------------- */
        .stButton > button, .stDownloadButton > button {{
            background: linear-gradient(90deg, {NAVY}, {STEEL});
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.65rem 1.4rem;
            font-weight: 600;
            font-size: 14.5px;
            box-shadow: 0 8px 18px rgba(11,60,109,0.22);
            transition: 0.2s;
        }}

        .stButton > button:hover, .stDownloadButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 12px 22px rgba(11,60,109,0.3);
            color: white;
            border: none;
        }}

        .stDownloadButton > button {{
            background: linear-gradient(90deg, {GOLD}, #E0B054);
            box-shadow: 0 8px 18px rgba(201,150,43,0.25);
        }}

        /* ---------------- Tabs ---------------- */
        .stTabs [data-baseweb="tab-list"] {{
            gap: 6px;
            background: {CARD};
            padding: 6px;
            border-radius: 14px;
            box-shadow: 0 4px 14px rgba(11,60,109,0.06);
        }}

        .stTabs [data-baseweb="tab"] {{
            border-radius: 10px;
            padding: 10px 18px;
            font-weight: 600;
            color: {MUTED};
        }}

        .stTabs [aria-selected="true"] {{
            background: linear-gradient(90deg, {NAVY}, {STEEL});
            color: white !important;
        }}

        /* ---------------- Inputs ---------------- */
        .stTextInput input {{
            border-radius: 10px !important;
            border: 1.5px solid {BORDER} !important;
        }}

        .stTextInput input:focus {{
            border-color: {STEEL} !important;
            box-shadow: 0 0 0 2px rgba(27,111,168,0.15) !important;
        }}

        /* ---------------- Native Streamlit metric override ---------------- */
        [data-testid="stMetric"] {{
            background: {CARD};
            border: 1px solid {BORDER};
            border-radius: 16px;
            padding: 16px 18px;
            box-shadow: 0 8px 20px rgba(11,60,109,0.07);
        }}

        [data-testid="stMetricLabel"] {{
            color: {MUTED};
            font-weight: 600;
        }}

        [data-testid="stMetricValue"] {{
            color: {NAVY};
            font-family: 'Poppins', sans-serif;
        }}

        /* ---------------- Dataframe wrapper ---------------- */
        [data-testid="stDataFrame"] {{
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(11,60,109,0.07);
            border: 1px solid {BORDER};
        }}

        /* ---------------- Divider ---------------- */
        hr {{
            border-color: {BORDER};
        }}

        /* ---------------- Footer ---------------- */
        .app-footer {{
            text-align: center;
            padding: 28px 10px 10px 10px;
            color: {MUTED};
        }}

        .app-footer .brand {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            color: {NAVY};
            font-size: 17px;
        }}

        .app-footer .tag {{
            font-size: 12.5px;
            margin-top: 6px;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


def render_sidebar(model_name="Random Forest Classifier", version="2.0"):
    """Renders the shared, branded sidebar content (below Streamlit's auto page nav)."""
    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-brand">
                <div class="icon">💳</div>
                <div>
                    <div class="title">Fraud Shield</div>
                    <div class="subtitle">AI Transaction Security</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="sidebar-badge">
                <div class="label">🤖 Active Model</div>
                <div class="value">{model_name}</div>
            </div>
            <div class="sidebar-badge">
                <div class="label">📦 Version</div>
                <div class="value">{version}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="sidebar-dev-card">
                <div class="name">👩‍💻 Memoona Abbas</div>
                <div class="role">BS Computer Science</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        st.info("📌 **Tip:** Use the Fraud Prediction page to analyze individual or batch transactions.")


def render_footer():
    st.markdown(
        """
        <div class="app-footer">
            <div class="brand">💳 Credit Card Fraud Detection System</div>
            <div class="tag">Developed by <b>Memoona Abbas</b></div>
            <div class="tag">Python • Scikit-learn • Streamlit • Machine Learning</div>
            <div class="tag" style="font-size:11.5px; margin-top:8px;">© 2026 All Rights Reserved</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
