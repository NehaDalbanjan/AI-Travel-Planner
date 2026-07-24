from flask import Flask, render_template, request, send_file

from services.dataset_service import (
    get_place_details,
    get_all_destinations
)
from services.expense_predictor import predict_expense
from services.hotel_dataset_service import get_hotel_details
from services.gemini_service import generate_itinerary
from services.pdf_service import create_pdf

app = Flask(__name__)


# ========================= HOME PAGE =========================

@app.route("/")
def home():

    destinations = get_all_destinations()

    return render_template(
        "index.html",
        destinations=destinations
    )


# ========================= TRIP PLANNER =========================

@app.route("/plan", methods=["POST"])
def plan():

    # Get form data
    source = request.form["source"]
    destination = request.form["destination"]
    days = request.form["days"]
    budget = request.form["budget"]
    transport = request.form["transport"]
    hotel_type = request.form["hotel_type"]
    travelers = request.form["travelers"]

    # Get destination details
    place = get_place_details(destination)

    if place is None:
        return f"Destination '{destination}' not found."

    first_place = place["first_place"]

    # Hotel Recommendation
    hotel = get_hotel_details(destination)

    # Expense Prediction
    predicted_expense = predict_expense(
        first_place["place_name"],
        first_place["category"],
        first_place["budget_tier"],
        first_place["days_recommended"],
        first_place["popularity_score"]
    )

    # AI Itinerary
    itinerary = generate_itinerary(
        source,
        destination,
        days,
        budget,
        transport,
        hotel_type,
        travelers
    )

    # Create PDF with ACTUAL trip details
    create_pdf(
        filename="trip_plan.pdf",
        source=source,
        destination=destination,
        days=days,
        travelers=travelers,
        transport=transport,
        hotel_type=hotel_type,
        budget=budget,
        prediction=predicted_expense,
        itinerary=itinerary
    )

    return render_template(
        "result.html",
        source=source,
        destination=destination,
        days=days,
        budget=budget,
        travelers=travelers,
        transport=transport,
        hotel_type=hotel_type,
        itinerary=itinerary,
        prediction=predicted_expense,
        place=place,
        first_place=first_place,
        hotel_details=hotel
    )


# ========================= DOWNLOAD PDF =========================

@app.route("/download")
def download():

    return send_file(
        "trip_plan.pdf",
        as_attachment=True
    )


# ========================= RUN APP =========================

if __name__ == "__main__":
    app.run(debug=True)