import streamlit as st
from theme import inject_base_css, render_sidebar, render_footer

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

inject_base_css()
render_sidebar()

# ============================================================
# Hero Section
# ============================================================

st.markdown("""
<div class="hero-card">
    <span class="eyebrow-light">AI-Powered Financial Security</span>
    <h1>💳 Credit Card Fraud Detection System</h1>
    <p>
    Detect fraudulent credit card transactions quickly and accurately using
    Machine Learning. Built for banks and financial institutions that need
    fast, reliable, and transparent fraud analysis.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Hero Image
# ============================================================

st.markdown('<div class="plain-card">', unsafe_allow_html=True)
st.image(
    "https://www.xenonstack.com/hubfs/xenonstack-credit-card-fraud-detection.png",
    use_container_width=True
)
st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# Project Overview
# ============================================================

st.markdown("""
<div class="premium-card">
<span class="eyebrow">Overview</span>
<h2 style="margin-top:0;">📖 Project Overview</h2>
<p style="color:#5B6B82; font-size:15px; line-height:1.7;">
Credit card fraud has become one of the biggest challenges in the financial
sector. This project uses a trained <b>Random Forest</b> machine learning
model to classify transactions as either legitimate or fraudulent. The
application provides both manual transaction prediction and batch prediction
using CSV files, making fraud analysis fast, accurate, and user-friendly.
</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Dataset Statistics
# ============================================================

st.header("📊 Dataset Statistics")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">📄</div>
    <div class="value">284,807</div>
    <div class="label">Total Transactions</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">🚨</div>
    <div class="value">492</div>
    <div class="label">Fraud Cases</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">🤖</div>
    <div class="value">Random Forest</div>
    <div class="label">ML Model</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ============================================================
# Key Features
# ============================================================

st.header("✨ Key Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📝</div>
    <h4>Manual Prediction</h4>
    <p>Predict a single credit card transaction instantly by entering its details.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📊</div>
    <h4>Interactive Charts</h4>
    <p>Visualize fraud distribution through clean, interactive charts.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📄</div>
    <h4>Batch Prediction</h4>
    <p>Upload CSV files and predict fraud across multiple transactions at once.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">⬇</div>
    <h4>Download Report</h4>
    <p>Export prediction results as a clean, ready-to-share CSV report.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ============================================================
# Project Workflow
# ============================================================

st.header("🔄 Project Workflow")

steps = [
    ("1", "Dataset Collection"),
    ("2", "Data Cleaning & Preprocessing"),
    ("3", "Feature Scaling"),
    ("4", "SMOTE Oversampling"),
    ("5", "Random Forest Model Training"),
    ("6", "Model Evaluation"),
    ("7", "Streamlit Deployment"),
]

steps_html = '<div class="premium-card"><span class="eyebrow">Pipeline</span>'
for i, (num, label) in enumerate(steps):
    steps_html += f"""
    <div class="step-row">
        <div class="step-num">{num}</div>
        <div class="step-label">{label}</div>
    </div>
    """
    if i < len(steps) - 1:
        steps_html += '<div class="step-connector"></div>'
steps_html += "</div>"

st.markdown(steps_html, unsafe_allow_html=True)

# ============================================================
# Footer
# ============================================================

st.divider()
render_footer()
