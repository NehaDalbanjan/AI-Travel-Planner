import pandas as pd

# Load dataset only once
df = pd.read_csv("data/travel_expenses_dataset.csv")


def get_all_destinations():
    return sorted(df["district"].unique().tolist())


def get_place_details(district):

    places = df[df["district"].str.lower() == district.lower()]

    if places.empty:
        return None

    return {
        "district": district,
        "places": places.to_dict(orient="records"),
        "first_place": places.iloc[0].to_dict()
    }