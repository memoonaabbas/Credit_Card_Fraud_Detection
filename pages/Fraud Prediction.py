import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.express as px

# ============================================================
# Page Configuration
# ============================================================

st.set_page_config(
    page_title="Fraud Prediction",
    page_icon="🔍",
    layout="wide"
)
# ============================================================
# Load Model
# ============================================================

model = joblib.load("models/random_forest_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# ============================================================
# Title
# ============================================================

st.title("🔍 Credit Card Fraud Prediction")

st.write(
    "Enter the transaction details below to predict whether the transaction is legitimate or fraudulent."
)

st.info("""
ℹ️ **About the Input Features**

- **Time** → Time elapsed since the first transaction in the dataset.
- **Amount** → Transaction amount.
- **V1–V28** → Anonymous features created using Principal Component Analysis (PCA) to protect customer privacy.
- These features preserve transaction patterns needed for fraud detection.
""")

# ============================================================
# Tabs
# ============================================================

tab1, tab2 = st.tabs(["📝 Manual Prediction", "📄 Batch Prediction"])

# ============================================================
# Manual Prediction
# ============================================================

with tab1:

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

    st.divider()

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

                st.error("🚨 Fraudulent Transaction Detected")

            else:

                st.success("✅ Legitimate Transaction")

            st.metric(
                "Model Confidence",
                f"{confidence:.2f}%"
            )

        except Exception as e:

            st.error(str(e))

# ============================================================
# Batch Prediction
# ============================================================

with tab2:

    st.subheader("📄 Batch Prediction")

    st.write("""
Upload a CSV file containing multiple credit card transactions.

The uploaded file must contain the same 30 input features used during model training.

Required Columns:
Time, V1 ... V28, Amount
""")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")

        st.write("### Preview")

        st.dataframe(df.head())

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

                st.subheader("📊 Prediction Summary")

                col1, col2, col3, col4 = st.columns(4)

                with col1:
                 st.metric(
                "📄 Total",
                total_transactions
                 )

                with col2:
                 st.metric(
                "✅ Safe",
                  safe_transactions
               )

                with col3:
                 st.metric(
                 "🚨 Fraud",
                  fraud_transactions
                )

                with col4:
                 st.metric(
                 "⚠️ Fraud Rate",
                   f"{fraud_rate:.2f}%"
               )
                 # ============================================================
                 # Prediction Message
                 # ============================================================

                if fraud_transactions == 0:

                 st.success(
                 f"""
                 🎉 **Analysis Completed**

                 All **{total_transactions} transactions** appear to be legitimate.

                No suspicious or fraudulent transactions were detected.
            """
            )

                else:

                 st.warning(
                f"""
               ⚠️ **Warning!**

                Out of **{total_transactions} transactions**,

              🚨 **{fraud_transactions}** transaction(s) appear to be suspicious.

               Please review these transactions carefully before taking any action.
               """
            )
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
                color="Category",
                color_discrete_map={
                "Safe": "green",
                "Fraud": "red"
                }
                )

                st.plotly_chart(fig, use_container_width=True)
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

                st.subheader("📋 Prediction Results")

                st.dataframe(
                    df[[
                        "Time",
                        "Amount",
                        "Status",
                        "Fraud Risk"
                    ]]
                )
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

st.markdown(
    """
<div style='text-align: center; color: gray; font-size:16px;'>

💳 <b>Credit Card Fraud Detection System</b><br><br>

Developed by <b>Memoona Abbas</b><br>

Machine Learning • Streamlit • Scikit-learn • Python

</div>
""",
unsafe_allow_html=True
)
