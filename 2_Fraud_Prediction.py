import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

from theme import inject_base_css, render_sidebar, render_footer, NAVY, STEEL, SUCCESS, DANGER

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Fraud Prediction",
    page_icon="🔍",
    layout="wide"
)

inject_base_css()
render_sidebar()

# ============================================================
# Load Model  (UNCHANGED)
# ============================================================

model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ============================================================
# Header
# ============================================================

st.markdown("""
<div class="hero-card">
    <span class="eyebrow-light">Real-Time Analysis</span>
    <h1>🔍 Credit Card Fraud Prediction</h1>
    <p>Enter transaction details below to predict whether a transaction is legitimate or fraudulent.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="plain-card">
<b>ℹ️ About the Input Features</b>
<ul style="color:#5B6B82; font-size:14px; line-height:1.8; margin-top:10px;">
<li><b>Time</b> → Time elapsed since the first transaction in the dataset.</li>
<li><b>Amount</b> → Transaction amount.</li>
<li><b>V1–V28</b> → Anonymous features created using Principal Component Analysis (PCA) to protect customer privacy.</li>
<li>These features preserve transaction patterns needed for fraud detection.</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ============================================================
# Tabs
# ============================================================

tab1, tab2 = st.tabs(["📝 Manual Prediction", "📄 Batch Prediction"])

# ============================================================
# Manual Prediction
# ============================================================

with tab1:

    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<span class="eyebrow">Step 1</span>', unsafe_allow_html=True)
    st.subheader("💳 Transaction Details")

    col1, col2 = st.columns(2)

    with col1:
        time = st.text_input(
            "Time",
            value="0.0",
            placeholder="e.g. 406"
        )

    with col2:
        amount = st.text_input(
            "Amount",
            value="0.0",
            placeholder="e.g. 149.62"
        )

    st.divider()

    with st.expander("📊 Principal Components (V1–V28)", expanded=False):

        features = []

        for row in range(7):

            cols = st.columns(4)

            for col in range(4):

                feature_num = row * 4 + col + 1

                with cols[col]:

                    value = st.text_input(
                        f"V{feature_num}",
                        value="0.0",
                        key=f"V{feature_num}"
                    )

                    try:
                        features.append(float(value))
                    except ValueError:
                        features.append(0.0)

    st.caption(
        "Fill in the transaction details and click Predict Transaction."
    )

    predict = st.button(
        "🔍 Predict Transaction",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<span class="eyebrow">Step 2</span>', unsafe_allow_html=True)
    st.subheader("📈 Prediction Result")

    if predict:

        try:

            time = float(time)
            amount = float(amount)

            input_data = [time] + features + [amount]

            input_array = np.array(input_data).reshape(1, -1)

            input_scaled = scaler.transform(input_array)

            prediction = model.predict(input_scaled)[0]

            probability = model.predict_proba(input_scaled)[0]

            confidence = max(probability) * 100

            if prediction == 1:

                st.markdown(f"""
                <div class="result-fraud">
                    <div class="result-icon">🚨</div>
                    <div>
                        <div class="result-title">Fraudulent Transaction Detected</div>
                        <div class="result-sub">This transaction shows patterns consistent with fraud. Review before approving.</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown(f"""
                <div class="result-safe">
                    <div class="result-icon">✅</div>
                    <div>
                        <div class="result-title">Legitimate Transaction</div>
                        <div class="result-sub">No fraud indicators detected for this transaction.</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

        except Exception as e:

            st.error(str(e))
    else:
        st.caption("Results will appear here after you click **Predict Transaction**.")

    st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# Batch Prediction
# ============================================================

with tab2:

    st.markdown('<div class="premium-card">', unsafe_allow_html=True)
    st.markdown('<span class="eyebrow">Batch Upload</span>', unsafe_allow_html=True)
    st.subheader("📄 Batch Prediction")

    st.write("""
Upload a CSV file containing multiple credit card transactions.

The uploaded file must contain the same 30 input features used during model training.

**Required Columns:** `Time, V1 ... V28, Amount`
""")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.markdown('<div class="plain-card">', unsafe_allow_html=True)
        st.write("### 👀 Preview")
        st.dataframe(df.head())
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🔍 Analyze Transactions"):

            try:

                scaled = scaler.transform(df)

                predictions = model.predict(scaled)

                probabilities = model.predict_proba(scaled)[:,1]

                df["Prediction"] = predictions

                df["Fraud Probability"] = probabilities

                st.success("Prediction Completed Successfully!")
                # ============================================================
                # Prediction Summary
                # ============================================================

                total_transactions = len(df)
                fraud_transactions = (df["Prediction"] == 1).sum()
                safe_transactions = (df["Prediction"] == 0).sum()
                fraud_rate = (fraud_transactions / total_transactions) * 100

                st.header("📊 Prediction Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.markdown(f"""
                    <div class="metric-tile">
                    <div class="icon">📄</div>
                    <div class="value">{total_transactions}</div>
                    <div class="label">Total Transactions</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="metric-tile">
                    <div class="icon">✅</div>
                    <div class="value">{safe_transactions}</div>
                    <div class="label">Safe Transactions</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="metric-tile">
                    <div class="icon">🚨</div>
                    <div class="value">{fraud_transactions}</div>
                    <div class="label">Fraud Transactions</div>
                    </div>
                    """, unsafe_allow_html=True)

                with col4:
                    st.markdown(f"""
                    <div class="metric-tile">
                    <div class="icon">⚠️</div>
                    <div class="value">{fraud_rate:.2f}%</div>
                    <div class="label">Fraud Rate</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.write("")

                # ============================================================
                # Prediction Message
                # ============================================================

                if fraud_transactions == 0:

                    st.markdown(f"""
                    <div class="result-safe">
                        <div class="result-icon">🎉</div>
                        <div>
                            <div class="result-title">Analysis Completed</div>
                            <div class="result-sub">All {total_transactions} transactions appear to be legitimate. No suspicious activity detected.</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                else:

                    st.markdown(f"""
                    <div class="result-fraud">
                        <div class="result-icon">⚠️</div>
                        <div>
                            <div class="result-title">Suspicious Activity Detected</div>
                            <div class="result-sub">Out of {total_transactions} transactions, {fraud_transactions} appear suspicious. Please review carefully before taking action.</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                # ============================================================
                # Fraud vs Safe Pie Chart
                # ============================================================

                chart_data = {
                    "Category": ["Safe", "Fraud"],
                    "Count": [safe_transactions, fraud_transactions]
                }

                fig = px.pie(
                    chart_data,
                    names="Category",
                    values="Count",
                    title="Fraud vs Safe Transactions",
                    hole=0.55,
                    color="Category",
                    color_discrete_map={
                        "Safe": SUCCESS,
                        "Fraud": DANGER
                    }
                )
                fig.update_layout(
                    font=dict(family="Inter, sans-serif", color=NAVY),
                    title_font=dict(family="Poppins, sans-serif", size=18, color=NAVY),
                    legend=dict(orientation="h", yanchor="bottom", y=-0.15),
                    margin=dict(t=60, b=20, l=10, r=10),
                    paper_bgcolor="rgba(0,0,0,0)",
                )

                st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                st.markdown('<span class="eyebrow">Fraud Risk Distribution</span>', unsafe_allow_html=True)
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

                # ============================================================
                # Make Results User-Friendly
                # ============================================================

                df["Status"] = df["Prediction"].map({
                    0: "✅ Safe",
                    1: "🚨 Fraud"
                })

                df["Fraud Risk"] = (
                    df["Fraud Probability"] * 100
                ).round(2).astype(str) + "%"

                st.markdown('<div class="premium-card">', unsafe_allow_html=True)
                st.markdown('<span class="eyebrow">Details</span>', unsafe_allow_html=True)
                st.subheader("📋 Prediction Results")

                st.dataframe(
                    df[[
                        "Time",
                        "Amount",
                        "Status",
                        "Fraud Risk"
                    ]],
                    use_container_width=True
                )
                st.markdown('</div>', unsafe_allow_html=True)

                # ============================================================
                # Create Download Report
                # ============================================================

                download_df = df[[
                    "Time",
                    "Amount",
                    "Status",
                    "Fraud Risk"
                ]].rename(columns={
                    "Time": "Transaction Time",
                    "Amount": "Transaction Amount"
                })
                csv = download_df.to_csv(index=False).encode("utf-8")

                st.download_button(
                    label="⬇ Download Prediction Report",
                    data=csv,
                    file_name="Fraud_Prediction_Report.csv",
                    mime="text/csv",
                    use_container_width=True
                )

            except Exception as e:

                st.error(e)

st.divider()
render_footer()
