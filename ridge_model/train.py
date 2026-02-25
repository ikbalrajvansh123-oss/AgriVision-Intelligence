# ===============================
# 1️⃣ IMPORT LIBRARIES
# ===============================

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# LOAD DATA


df = pd.read_csv("crop-yield/crop_data.csv")

print("Dataset Shape:", df.shape)
print(df.columns)

#  BASIC CLEANING


# Drop ID column
df = df.drop(columns=["ID"])

# Separate features & target
X = df.drop("Crop_Yield (kg/ha)", axis=1)
y = df["Crop_Yield (kg/ha)"]


#  TRAIN TEST SPLIT


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


#  PREPROCESSING SETUP


numeric_features = ['Year', 'Rainfall (mm)', 'Irrigation_Area (ha)']
categorical_features = ['State', 'Crop_Type', 'Soil_Type']

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])


#  PIPELINE (RIDGE MODEL)


model = Pipeline([
    ("preprocess", preprocessor),
    ("model", Ridge(alpha=10))
])


#  TRAIN MODEL


model.fit(X_train, y_train)

#  EVALUATION


train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("\n📊 Model Performance")
print("Train R2:", r2_score(y_train, train_pred))
print("Test R2:", r2_score(y_test, test_pred))
print("MAE:", mean_absolute_error(y_test, test_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, test_pred)))

# MAPE
mape = np.mean(np.abs((y_test - test_pred) / y_test)) * 100
print("MAPE:", round(mape,2), "%")


# CROSS VALIDATION


cv_scores = cross_val_score(model, X, y, cv=5, scoring="r2")

print("\nCV R2 Scores:", cv_scores)
print("Average CV R2:", np.mean(cv_scores))

# SAVE MODEL

joblib.dump(model, "crop_yield_ridge_pipeline.pkl")
print("\n✅ Model Saved Successfully!")


