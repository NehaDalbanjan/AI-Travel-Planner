import pandas as pd

hotel_df = pd.read_csv("data/hotels_places.csv")


def get_hotel_details(district):

    district = district.strip().lower()

    # Exact match
    hotel = hotel_df[
        hotel_df["District"].str.strip().str.lower() == district
    ]

    if not hotel.empty:
        return hotel.iloc[0].to_dict()

    # Partial match (handles Bengaluru -> Bengaluru Urban)
    hotel = hotel_df[
        hotel_df["District"].str.strip().str.lower().str.contains(district)
    ]

    if not hotel.empty:
        return hotel.iloc[0].to_dict()

    return None