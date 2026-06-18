import streamlit as st
import pandas as pd
import joblib

model = joblib.load("house_price_model.pkl")
transform = joblib.load("preprocessor.pkl")

st.title("🏠 House Price Prediction")
st.caption("Developed by Vipul Gupta | Machine Learning Project")

area = st.number_input("Area", value=5000)
bedrooms = st.number_input("Bedrooms", value=3)
bathrooms = st.number_input("Bathrooms", value=2)
stories = st.number_input("Stories", value=2)
parking = st.number_input("Parking", value=1)

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

if st.button("Predict"):

    data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "stories":[stories],
        "mainroad":[mainroad],
        "guestroom":[guestroom],
        "basement":[basement],
        "hotwaterheating":[hotwaterheating],
        "airconditioning":[airconditioning],
        "parking":[parking],
        "prefarea":[prefarea],
        "furnishingstatus":[furnishingstatus]
    })

    data = transform.transform(data)
    prediction = model.predict(data)

    st.success(f"Predicted Price: ₹{prediction[0]:,.0f}")