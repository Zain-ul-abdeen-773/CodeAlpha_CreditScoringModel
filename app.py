from flask import Flask, render_template, request
import joblib
import os
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("best_model.pkl")

@app.route('/')
def index():
    plots = [f for f in os.listdir('static/plots') if f.endswith('.png')]
    table = pd.read_csv("models/model_performance.csv").to_html(
        classes='table table-dark table-striped text-center',
        index=False,
        border=0
    )
    return render_template("index.html", plots=plots, table=table)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get 3 user inputs
            age = float(request.form['age'])
            income = float(request.form['income'])
            credit_cards = float(request.form['credit_cards'])

            # Fill remaining 32 values with sample/defaults
            # 👇 Make sure this contains EXACTLY 32 values
            other_features = [
             5, 0, 3, 2, 0.5, 1, 1, 1, 1, 1,
             0, 0.3, 24, 1, 0, 1, 5000, 1000, 0,
             1, 3, 1, 1, 2, 10000, 0.2, 1, 0, 1,
             2000, 200  ,1
             ]


            # Merge all into one feature list
            features = [age, income, credit_cards] + other_features

            # Predict using the model
            prediction = model.predict([features])[0]
            label_map = {0: "Poor", 1: "Standard", 2: "Good"}
            label = label_map.get(prediction, "Unknown")
            return render_template("result.html", pred=label)


        except Exception as e:
            return f"Prediction Error: {e}"

    return render_template("predict.html")

if __name__ == '__main__':
    app.run(debug=True)
