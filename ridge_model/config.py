

# Data Path
DATA_PATH = "data/crop_data.csv"

# Target Column
TARGET_COLUMN = "Crop_Yield (kg/ha)"

# Numeric Features
NUMERIC_FEATURES = [
    'Year',
    'Rainfall (mm)',
    'Irrigation_Area (ha)'
]

# Categorical Features
CATEGORICAL_FEATURES = [
    'State',
    'Crop_Type',
    'Soil_Type'
]

# Model Saving Path
MODEL_PATH = "models/crop_yield_ridge_v1.pkl"

# Random State
RANDOM_STATE = 42

# Test Size
TEST_SIZE = 0.2