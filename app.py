import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


st.title("🏠 House Price Prediction App")
st.write("Predict house prices  using a Machine Learning model trained with Gradient Boosting Regressor.")

st.markdown("---")


with st.expander("📊 Model Information"):
    st.write("""
    - **Algorithm:** Gradient Boosting Regressor  
    - **Type:** Supervised Machine Learning (Regression)  
    - **Objective:** Predict house prices based on input features  
    - **Strength:** Handles non-linear relationships very well  
    - **Training:** Model trained on cleaned housing dataset  
    """)


model = joblib.load("house_price_model.pkl")


st.subheader("📥 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area (sq ft)", min_value=500, max_value=100000, value=1500)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=20, value=3)

with col2:
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=20, value=2)
    location_score = st.number_input("Location Score (1-10)", min_value=1, max_value=20, value=5)

st.markdown("---")


if st.button("🔮 Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, location_score]])
    prediction = model.predict(input_data)

    st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")

#
st.markdown("---")
st.caption("Built with Streamlit by Vipul Gupta | ML Project - House Price Prediction")