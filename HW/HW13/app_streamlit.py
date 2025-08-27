import streamlit as st
import pickle
import numpy as np

st.title("Model Prediction Dashboard")

with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

input1 = st.number_input("Feature 1", value=0.0)
input2 = st.number_input("Feature 2", value=0.0)

if st.button("Predict"):
    prediction = model.predict([[input1, input2]])[0]
    st.write(f"Prediction: {prediction:.3f}")
