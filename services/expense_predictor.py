import joblib
import pandas as pd

# Load the trained model once when the app starts
model = joblib.load("models/expense_model.pkl")


def predict_expense(place_name, category, budget_tier, days_recommended, popularity_score):
    data = pd.DataFrame({
        "place_name": [place_name],
        "category": [category],
        "budget_tier": [budget_tier],
        "days_recommended": [days_recommended],
        "popularity_score": [popularity_score]
    })

    prediction = model.predict(data)

    return round(prediction[0], 2)