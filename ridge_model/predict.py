import joblib
import pandas as pd
import config

# Load Model
model = joblib.load(config.MODEL_PATH)

sample_data = {
    "Year": [2025],
    "Rainfall (mm)": [800],
    "Irrigation_Area (ha)": [1200],
    "State": ["Punjab"],
    "Crop_Type": ["Wheat"],
    "Soil_Type": ["Loamy"]
}

input_df = pd.DataFrame(sample_data)

# Predict
prediction = model.predict(input_df)

print("\n🌾 Predicted Crop Yield (kg/ha):", prediction[0])