from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)

# Cargar modelo
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    bmi = float(request.form["bmi"])
    children = int(request.form["children"])
    sex = request.form["sex"]
    smoker = request.form["smoker"]
    region = request.form["region"]

    df = pd.DataFrame([{
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex": sex,
        "smoker": smoker,
        "region": region
    }])

    prediction = model.predict(df)[0]

    return render_template("result.html", prediction=round(prediction, 2))

if __name__ == "__main__":
    app.run(debug=True)
