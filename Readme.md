# 🌾 AgriVision Analytics  
### AI-Powered Crop Yield Forecasting Platform

AgriVision Analytics is a machine learning-based crop yield prediction system designed to assist agricultural planners, policymakers, and agribusiness stakeholders in forecasting crop production using historical and environmental data.

The platform leverages a trained Ridge Regression pipeline model to generate accurate and reliable crop yield forecasts with an average MAPE of approximately 7.68%.

---

## 🚀 Features

- 📊 Crop yield prediction (kg/ha)
- 📈 Confidence interval estimation
- 🌍 Multi-state support (Punjab, Haryana, Uttar Pradesh, Bihar)
- 🌾 Multi-crop support (Wheat, Rice, Maize, Cotton)
- 🌱 Soil type consideration
- 🌧 Rainfall impact analysis
- 🚿 Irrigation impact modeling
- 🎨 Clean, industry-level Streamlit dashboard UI

---

## 🧠 Machine Learning Model

- Model Type: Ridge Regression Pipeline
- Preprocessing: Categorical encoding + numerical scaling
- Error Metric: Mean Absolute Percentage Error (MAPE ≈ 7.68%)
- Deployment Ready: Yes

The model was trained on structured agricultural datasets incorporating:
- Year
- State
- Crop Type
- Soil Type
- Rainfall (mm)
- Irrigation Area (ha)

---

## 🖥️ Application Architecture

AgriVision Analytics is built using:

- Python
- Streamlit (Frontend + Deployment)
- Scikit-learn
- Pandas
- Joblib

Workflow:

User Input → DataFrame Creation → Model Prediction → Confidence Interval Calculation → Dashboard Display

---



## 📊 Example Prediction Output

- Predicted Yield (kg/ha)
- Lower Estimate (Confidence Interval)
- Upper Estimate
- Model Confidence Level

---

## 🌐 Deployment

This application can be deployed using:

- Streamlit Cloud
- AWS EC2
- Azure App Service
- Heroku

---

## 📈 Industry Use Cases

- Agricultural policy planning
- Crop production forecasting
- Risk analysis for agribusiness
- Yield optimization research
- Irrigation impact modeling

---

## 🔒 Limitations

- Predictions depend on training data quality.
- Does not incorporate real-time satellite or weather APIs (future enhancement).
- Suitable for regional-level forecasting, not micro-farm precision modeling.

---

## 🔮 Future Enhancements

- Real-time weather API integration
- Satellite imagery data incorporation
- Advanced ensemble models (XGBoost, LightGBM)
- Trend visualization dashboard
- Exportable PDF reports
- Multi-user authentication system

---

## 👨‍💻 Author

Developed as an AI-powered agricultural analytics solution.

---

## 📜 License

This project is intended for research and educational purposes.  
Commercial deployment may require further validation and domain-specific calibration.
