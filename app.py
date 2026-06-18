import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


st.title("🏠 House Price Prediction App")
st.write("ML model trained using Gradient Boosting with full feature preprocessing pipeline.")

st.markdown("---")


with st.expander("📊 Model Information"):
    st.write("""
    - **Algorithm:** Gradient Boosting Regressor  
    - **Pipeline:** Includes preprocessing (encoding + scaling)  
    - **Input Type:** Numerical + Categorical features  
    - **Goal:** Predict accurate house prices based on multiple features like are,bathrooms,bedrooms,parking etc.
    """)


model = joblib.load("house_price_model.pkl")
transform = joblib.load("preprocessor.pkl")


st.subheader("📥 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area", value=5000)
    bedrooms = st.number_input("Bedrooms", value=3)
    bathrooms = st.number_input("Bathrooms", value=2)
    stories = st.number_input("Stories", value=2)
    parking = st.number_input("Parking", value=1)

with col2:
    mainroad = st.selectbox("Main Road", ["yes", "no"])
    guestroom = st.selectbox("Guest Room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot Water Heating", ["yes", "no"])
    airconditioning = st.selectbox("Air Conditioning", ["yes", "no"])
    prefarea = st.selectbox("Preferred Area", ["yes", "no"])

furnishingstatus = st.selectbox(
    "Furnishing Status",
    ["unfurnished", "semi-furnished", "furnished"]
)

st.markdown("---")


if st.button("🔮 Predict Price"):

    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    processed_data = transform.transform(input_data)
    prediction = model.predict(processed_data)

    st.success(f"💰 Predicted Price: ₹ {prediction[0]:,.0f}")


st.markdown("---")
st.caption("Built with Streamlit by Vipul Gupta | Gradient Boosting Regression Project")