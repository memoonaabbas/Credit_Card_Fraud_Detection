import streamlit as st
from theme import inject_base_css, render_sidebar, render_footer

st.set_page_config(page_title="About", page_icon="📘", layout="wide")

inject_base_css()
render_sidebar()

# ============================================================
# Hero
# ============================================================

st.markdown("""
<div class="hero-card">
    <span class="eyebrow-light">Project Documentation</span>
    <h1>📘 About the Project</h1>
    <p>A complete look at the goals, dataset, technology stack, and workflow behind this fraud detection system.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Project Overview
# ============================================================

st.markdown("""
<div class="premium-card">
<span class="eyebrow">Overview</span>
<h2 style="margin-top:0;">💳 Credit Card Fraud Detection using Machine Learning</h2>
<p style="color:#5B6B82; font-size:15px; line-height:1.75;">
This project aims to detect fraudulent credit card transactions using
Machine Learning techniques. Due to the highly imbalanced nature of the
dataset, <b>SMOTE</b> (Synthetic Minority Oversampling Technique) was applied
before model training.
</p>
<p style="color:#5B6B82; font-size:15px; line-height:1.9;">
The project includes:
</p>
<ul style="color:#5B6B82; font-size:14.5px; line-height:1.9;">
<li>Data Cleaning</li>
<li>Exploratory Data Analysis (EDA)</li>
<li>Feature Engineering</li>
<li>Feature Scaling</li>
<li>SMOTE Oversampling</li>
<li>Machine Learning Model Training</li>
<li>Model Evaluation</li>
<li>Streamlit Deployment</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.info("""
This application uses a Machine Learning model to identify potentially
fraudulent credit card transactions. Users can perform both manual and
batch predictions through an easy-to-use interface.
""")

# ============================================================
# Dataset Information
# ============================================================

st.header("📊 Dataset Information")

col1, col2, col3, col4 = st.columns(4)

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
    <div class="icon">✅</div>
    <div class="value">284,315</div>
    <div class="label">Legitimate Cases</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">⚠️</div>
    <div class="value">0.17%</div>
    <div class="label">Fraud Rate</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">🧬</div>
    <div class="value">30</div>
    <div class="label">Features</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-tile">
    <div class="icon">🎯</div>
    <div class="value">Class</div>
    <div class="label">Target Variable</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ============================================================
# Technologies Used
# ============================================================

st.header("🛠 Technologies Used")

tech = ["Python", "Pandas", "NumPy", "Matplotlib", "Seaborn",
        "Plotly", "Scikit-learn", "Imbalanced-learn (SMOTE)", "Joblib", "Streamlit"]

tech_html = '<div class="premium-card"><span class="eyebrow">Stack</span><div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:12px;">'
for t in tech:
    tech_html += f"""<div style="background:#EAF4FF; border:1px solid #D9E6F5; color:#0B3C6D;
    font-weight:600; font-size:13.5px; padding:8px 16px; border-radius:999px;">{t}</div>"""
tech_html += "</div></div>"

st.markdown(tech_html, unsafe_allow_html=True)

# ============================================================
# Project Workflow
# ============================================================

st.header("🔄 Project Workflow")

workflow_steps = [
    ("1", "Dataset Collection"),
    ("2", "Data Cleaning"),
    ("3", "Exploratory Data Analysis"),
    ("4", "Feature Scaling"),
    ("5", "SMOTE Oversampling"),
    ("6", "Model Training"),
    ("7", "Model Evaluation"),
    ("8", "Model Deployment"),
]

wf_html = '<div class="premium-card"><span class="eyebrow">Pipeline</span>'
for i, (num, label) in enumerate(workflow_steps):
    wf_html += f"""
    <div class="step-row">
        <div class="step-num">{num}</div>
        <div class="step-label">{label}</div>
    </div>
    """
    if i < len(workflow_steps) - 1:
        wf_html += '<div class="step-connector"></div>'
wf_html += "</div>"

st.markdown(wf_html, unsafe_allow_html=True)

# ============================================================
# Machine Learning Model
# ============================================================

st.header("🤖 Machine Learning Model")

st.markdown("""
<div class="premium-card">
<span class="eyebrow">Model</span>
<p style="color:#5B6B82; font-size:15px; line-height:1.75; margin-top:10px;">
The application uses a <b>Random Forest Classifier</b> trained on a balanced
dataset created using <b>SMOTE</b>. The trained model predicts whether a
transaction is <b>Legitimate</b> or <b>Fraudulent</b> based on the provided
transaction features.
</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Prediction Features
# ============================================================

st.header("✨ Prediction Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📝</div>
    <h4>Manual Transaction Prediction</h4>
    <p>Instant fraud check for a single transaction.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">🎯</div>
    <h4>Fraud Risk Percentage</h4>
    <p>Clear confidence score for every prediction.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📄</div>
    <h4>Batch CSV Prediction</h4>
    <p>Analyze thousands of transactions in one upload.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="feature-card">
    <div class="f-icon">📊</div>
    <h4>Interactive Pie Chart &amp; Report</h4>
    <p>Visual breakdown plus a downloadable prediction report.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ============================================================
# How to Use
# ============================================================

st.subheader("📖 How to Use")

how_to = [
    ("1", "Open the Fraud Prediction page."),
    ("2", "Choose Manual Prediction or Batch Prediction."),
    ("3", "Enter transaction details or upload a CSV file."),
    ("4", "Click Analyze Transactions."),
    ("5", "Review the prediction summary, charts, and detailed results."),
    ("6", "Download the prediction report if needed."),
]

how_html = '<div class="premium-card"><span class="eyebrow">Guide</span>'
for i, (num, label) in enumerate(how_to):
    how_html += f"""
    <div class="step-row">
        <div class="step-num">{num}</div>
        <div class="step-label">{label}</div>
    </div>
    """
    if i < len(how_to) - 1:
        how_html += '<div class="step-connector"></div>'
how_html += "</div>"

st.markdown(how_html, unsafe_allow_html=True)

st.divider()
render_footer()
