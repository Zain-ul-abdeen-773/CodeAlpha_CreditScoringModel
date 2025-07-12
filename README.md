# 🧠 CodeAlpha_CreditScoringModel

## 📌 Objective
This project predicts an individual's **creditworthiness** using historical financial data by classifying them as a **good** or **bad credit risk**. The solution combines **data analysis**, **ML modeling**, and a **Flask web app** for visualizing results.

---

## 🚀 Project Summary
As part of the CodeAlpha Internship, this project includes:
- Detailed **Exploratory Data Analysis (EDA)**
- Feature engineering from financial history
- Model building (Logistic Regression, Decision Tree, Random Forest)
- Performance evaluation (Precision, Recall, F1-Score, ROC-AUC)
- A user-friendly **Flask-based dashboard** to visualize predictions and plots

---

## 📂 Dataset
Using the **German Credit Data** from UCI ML Repository:

- 📊 1,000 instances
- 📈 20 features (e.g., age, income, job, credit history)
- 🎯 Target: Credit Risk (Good/Bad)

> ✅ Dataset: [Credit Score Classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification 
)

---

## 📊 Exploratory Data Analysis (EDA)

EDA is structured into the following notebook tabs:

1. **Overview & Null Values**
2. **Univariate Analysis (histograms, value counts)**
3. **Bivariate Analysis (feature vs target)**
4. **Correlation Matrix and Heatmap**
5. **Feature Engineering**
6. **Encoding & Scaling**
7. **Train/Test Split**

> 📁 Outputs stored in `plots/` folder and displayed in Flask app

---

## 🧠 ML Models

| Model            | Description                          |
|------------------|--------------------------------------|
| LogisticRegression | Simple linear classifier            |
| DecisionTree       | Non-linear splits, good for trees   |
| RandomForest       | Ensemble of decision trees          |

---

## 🧪 Evaluation Metrics

Each model is evaluated using:

- ✅ Accuracy  
- ✅ Precision  
- ✅ Recall  
- ✅ F1-Score  
- ✅ ROC-AUC  
- ✅ Confusion Matrix  

> 📈 Graphs for ROC and Confusion Matrix are also viewable in the Flask app.

---

## 🌐 Flask Web App

### 📍 Features:
- Upload new data for prediction
- View **model prediction**
- Display **EDA plots** and **metrics**
- View **ROC curve** and **confusion matrix**

### ▶ How to Run Flask App

```bash
# Step 1: Clone repository
git clone https://github.com/Zain-ul-abdeen-773/CodeAlpha_CreditScoringModel.git
cd CodeAlpha_CreditScoringModel

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Run Flask app
python app.py
```
# Folder Structure 

```
CodeAlpha_CreditScoringModel/
│
├── app.py                  # Flask app main script
├── templates/
│   ├── index.html
│   ├── result.html
│
├── static/
│   ├── images/             # All EDA & model graphs
│
├── dataset/
│   └── german_credit_data.csv
│
├── notebooks/
│   └── credit_scoring_model.ipynb
│
├── models/
│   └── model.pkl           # Trained ML model
│
├── plots/
│   ├── correlation_heatmap.png
│   ├── roc_curve.png
│   ├── confusion_matrix.png
│
├── requirements.txt
└── README.md
```

## 🙌 Acknowledgement
Built during the CodeAlpha Internship Program

👨‍💻 Author
Zain ul Abdeen
- 📫 zainfaisalblock8@gmail.com
- 🔗 https://github.com/Zain-ul-abdeen-773

