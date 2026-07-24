import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("data/travel_expenses_dataset.csv")

# Features used for prediction
X = df[
    [
        "place_name",
        "category",
        "budget_tier",
        "days_recommended",
        "popularity_score"
    ]
]

# Target
y = df["total_max_cost"]

# Categorical columns
categorical_features = [
    "place_name",
    "category",
    "budget_tier"
]

# Numerical columns
numerical_features = [
    "days_recommended",
    "popularity_score"
]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "num",
            "passthrough",
            numerical_features
        )
    ]
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)

# Train
pipeline.fit(X, y)

# Save model
joblib.dump(pipeline, "models/expense_model.pkl")

print("✅ Expense prediction model trained successfully!")
print("✅ Model saved as models/expense_model.pkl")