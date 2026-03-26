import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("📊 Customer Churn Prediction")
st.write("Aplikasi ini memprediksi kemungkinan customer berhenti berlangganan.")

# Load model artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoder = joblib.load("encoder.pkl")

st.subheader("🧾 Masukkan Data Customer")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (Months)", 0, 72, 12)

with col2:
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check",
        "Bank transfer (automatic)", "Credit card (automatic)"
    ])

if st.button("🔮 Predict Churn"):

    input_df = pd.DataFrame([{
        "Gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "Tenure": tenure,
        "MonthlyCharges": monthly,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment
    }])

    categorical_cols = ["Gender", "Partner", "Dependents",
                        "Contract", "PaperlessBilling", "PaymentMethod"]
    numerical_cols = ["Tenure", "MonthlyCharges"]
    binary_cols = ["SeniorCitizen"]

    encoded_cat = encoder.transform(input_df[categorical_cols].values)
    scaled_num = scaler.transform(input_df[numerical_cols].values)
    bin_data = input_df[binary_cols].values

    final_input = np.hstack((scaled_num, encoded_cat, bin_data))

    pred = model.predict(final_input)[0]
    prob = model.predict_proba(final_input)[0][1]

    st.subheader("📢 Prediction Result")

    if pred == 1:
        st.error(f"⚠️ Customer Berpotensi Churn (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Customer Tidak Churn (Probability: {prob:.2%})")
    
    import warnings
    warnings.filterwarnings("ignore")
