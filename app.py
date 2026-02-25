import streamlit as st
import pandas as pd
import joblib
import time

# Page Config
st.set_page_config(
    page_title="AgriVision Analytics",
    page_icon="🌾",
    layout="wide"
)

# Minimal Clean CSS

st.markdown("""
<style>

/* Background */
.stApp {
    background: #f4f6f9;
}

/* Main container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Card style */
.simple-card {
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Button */
div.stButton > button {
    background-color: #1f77b4;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #155a8a;
}

/* Metric container */
[data-testid="metric-container"] {
    background: #ffffff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)


# Load Model

model = joblib.load("models/crop_yield_ridge_pipeline.pkl")


# Header

st.title("🌾 AgriVision Analytics")
st.caption("Smart Crop Yield Forecasting Platform")

st.divider()


# Input Section

st.markdown('<div class="simple-card">', unsafe_allow_html=True)

st.subheader("Input Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    year = st.slider("Year", 2000, 2035, 2023)
    rainfall = st.slider("Rainfall (mm)", 0, 2000, 600)

with col2:
    state = st.selectbox("State",
        ["Punjab", "Haryana", "Uttar Pradesh", "Bihar"])
    soil_type = st.selectbox("Soil Type",
        ["Clay", "Sandy", "Loamy"])

with col3:
    crop_type = st.selectbox("Crop Type",
        ["Wheat", "Rice", "Maize", "Cotton"])
    irrigation = st.slider("Irrigation Area (ha)", 0, 1000, 100)

st.write("")
predict_button = st.button("Generate Forecast")

st.markdown('</div>', unsafe_allow_html=True)


# Prediction Section

if predict_button:

    with st.spinner("Generating forecast..."):

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)

        input_df = pd.DataFrame({
            "Year": [year],
            "State": [state],
            "Crop_Type": [crop_type],
            "Rainfall (mm)": [rainfall],
            "Soil_Type": [soil_type],
            "Irrigation_Area (ha)": [irrigation]
        })

        prediction = model.predict(input_df)[0]

        error_margin = prediction * 0.0768
        lower = prediction - error_margin
        upper = prediction + error_margin

    st.markdown('<div class="simple-card">', unsafe_allow_html=True)

    st.subheader("Forecast Results")

    col1, col2, col3 = st.columns(3)

    col1.metric("Predicted Yield (kg/ha)", f"{prediction:.2f}")
    col2.metric("Lower Estimate", f"{lower:.2f}")
    col3.metric("Upper Estimate", f"{upper:.2f}")

    st.success("Model Confidence: High (MAPE ≈ 7.68%)")

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("Adjust input parameters and click 'Generate Forecast' to see results.")
