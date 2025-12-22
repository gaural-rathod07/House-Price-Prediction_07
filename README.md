# 🏠 California Housing Price Prediction

A machine learning web application that predicts the **median house value in California** based on geographical and demographic features.  
The project uses a **Random Forest Regressor** trained on the California Housing dataset and is deployed using **Flask** with a clean, responsive UI.

---

## 🚀 Features
- Predicts median house prices based on user input
- Machine learning model trained using Random Forest
- Data preprocessing with Scikit-learn Pipelines
- One-hot encoding for categorical features
- Flask-based web interface
- Responsive and modern UI using HTML & CSS

---

## 🛠 Tech Stack
- **Python**
- **Flask**
- **Scikit-learn**
- **Pandas, NumPy**
- **HTML, CSS**
- **Joblib**

---

## 📊 Dataset
The dataset used in this project is the **California Housing Prices** dataset, available on Kaggle:

https://www.kaggle.com/datasets/camnugent/california-housing-prices

This dataset is publicly available on Kaggle and is commonly used for educational and machine learning projects.

---

## ⚙️ Project Structure
```
House-Price-Prediction/
│
├── app.py # Flask application
├── main.py # Model training and inference
├── requirements.txt # Dependencies
├── README.md
│
├── model/
│ ├── model.pkl # Trained ML model
│ └── pipeline.pkl # Preprocessing pipeline
│
├── static/
│ ├── style.css
│ └── Theme*.png
│
├── templates/
│ ├── index.html
│ └── result.html
│
├── housing.csv # Dataset
└── .gitignore
```
---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/gaural-rathod07/House-Price-Prediction_07.git  
cd House Price Prediction

### 2️⃣ Create virtual environment (optional but recommended)
python -m venv myenv  
source myenv/bin/activate  # On Windows: myenv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the Flask app
python app.py

### 5️⃣ Open in browser
http://127.0.0.1:5000/

---

## 📈 Model Details

The trained model file is not included in the repository due to GitHub size limits.
Users can retrain the model by running main.py.

Algorithm: Random Forest Regressor

Preprocessing:

Median imputation for missing values

Feature scaling using StandardScaler

One-hot encoding for categorical features

Evaluation:

Cross-validation using RMSE

---

## 📌 Future Improvements

Model performance visualization

Deployment on cloud (Render / Railway / AWS)

Input validation and error handling

Additional feature engineering

---

## 👨‍💻 Author

Gaural Rathod
Data Analyst / Data Scientist
