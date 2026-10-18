# Insurance Premium Prediction API

A machine learning-powered application that predicts insurance premium categories using **FastAPI, Scikit-learn, and Streamlit**.

## 🌐 Live Demo

- **Streamlit App:** [Try the application](https://insurance-premium-prediction-yuvii.streamlit.app/)
- **FastAPI Backend:** [Open API](https://insurance-premium-prediction-api-backend.onrender.com)
- **API Documentation:** [Swagger UI](https://insurance-premium-prediction-api-backend.onrender.com/docs)
- **Health Check:** [Check API Status](https://insurance-premium-prediction-api-backend.onrender.com/health)

## 🚀 Key Features

- Machine learning-based insurance premium category prediction.
- REST API built with FastAPI.
- Interactive web interface built with Streamlit.
- Automatic input validation using Pydantic.
- Derived features including BMI, age group, lifestyle risk, and city tier.
- Interactive API documentation through Swagger UI.

## 🔌 API Endpoint

**Method:** `POST`

**Endpoint:**
`https://insurance-premium-prediction-api-backend.onrender.com/predict`

The API accepts customer information, including age, weight, height, annual income, smoking status, city, and occupation, and returns a predicted insurance premium category.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **API Framework:** FastAPI
- **Frontend:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Data Validation:** Pydantic
- **Deployment:** Render and Streamlit Community Cloud

## ⚙️ Architecture

1. Users enter their details in the Streamlit application.
2. The frontend sends the input to the FastAPI backend.
3. The backend validates the data and derives relevant features.
4. The trained machine learning model generates a prediction.
5. The predicted premium category is displayed in the frontend.

## 📌 Note

The free-tier backend may take some time to respond after a period of inactivity.
