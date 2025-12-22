from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

model = joblib.load("model/model.pkl")
pipeline = joblib.load("model/pipeline.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        # Collect input values from form
        input_data = {
            "longitude": float(request.form["longitude"]),
            "latitude": float(request.form["latitude"]),
            "housing_median_age": float(request.form["housing_median_age"]),
            "total_rooms": float(request.form["total_rooms"]),
            "total_bedrooms": float(request.form["total_bedrooms"]),
            "population": float(request.form["population"]),
            "households": float(request.form["households"]),
            "median_income": float(request.form["median_income"]),
            "ocean_proximity": request.form["ocean_proximity"],
        }

        df = pd.DataFrame([input_data])

        transformed = pipeline.transform(df)
        pred = model.predict(transformed)[0]
        prediction = round(pred, 2)

    return render_template("index.html", prediction=prediction)
    

if __name__ == "__main__":
    app.run(debug=True)
