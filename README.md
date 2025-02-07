# Amazon Delivery Time Prediction

## 📌 Project Overview
This project predicts the **estimated delivery time** for Amazon orders based on various factors such as agent details, weather conditions, traffic levels, and distance. The model is trained using regression techniques and deployed as a **Streamlit web application**.

## 🛠️ Technologies Used
- **Python** (Data Processing & Modeling)
- **Pandas, NumPy** (Data Handling)
- **XGBoost** (Machine Learning Model)
- **MLflow** (Model Tracking & Management)
- **Streamlit** (Web Application)

## 📂 Project Structure
```
📦 Amazon-Delivery-Time-Prediction
├── data/                # Dataset (Training & Testing)
├── models/              # Trained ML models (Pickle files)
├── notebooks/           # Jupyter Notebooks (Exploration & Training)
├── app.py               # Streamlit Application
├── requirements.txt     # Dependencies
├── README.md            # Project Documentation
```

## 🚀 How to Run the Project
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

## 🏗️ Features
✅ User-friendly **Streamlit** interface  
✅ Predicts delivery time based on multiple input factors  
✅ MLflow for model tracking & comparison  
✅ Uses the best-trained XGBoost model  

## 📊 Model Details
- **Algorithm:** XGBoost Regressor
- **Evaluation Metric:** R² Score
- **Feature Set:**
  - Agent Age, Agent Rating, Weather, Vehicle Type, Area Type
  - Distance (km), Traffic Level, Category, Pickup Time (min)

## 📌 Sample Prediction
| Agent Age | Agent Rating | Weather | Vehicle | Area | Distance (km) | Traffic | Category | Pickup Time (min) | Predicted Time (min) |
|-----------|-------------|---------|---------|------|--------------|---------|----------|------------------|------------------|
| 50        | 1.9         | 2       | 0       | 2    | 25           | 2       | 1        | 55               | 151.90           |


