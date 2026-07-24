import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_itinerary(
    source,
    destination,
    days,
    budget,
    transport,
    hotel_type,
    travelers
):

    prompt = f"""
You are an expert AI Travel Planner.

Create a beautiful and easy-to-read travel itinerary.

Trip Details

Source: {source}
Destination: {destination}
Days: {days}
Budget: ₹{budget}
Transport: {transport}
Hotel Type: {hotel_type}
Travelers: {travelers}

STRICT RULES

1. Use ONLY the selected transport: {transport}.
2. Never suggest any other transport.
3. If transport is Bus, never mention Train.
4. If transport is Train, never mention Bus.
5. If transport is Car, use only Car.
6. Recommend hotels only according to the selected hotel type.
7. Keep the entire plan within the given budget.
8. Mention approximate expenses wherever possible.

VERY IMPORTANT

DO NOT use Markdown.

Do NOT use:
###
##
**
*
---
>

Instead, write in plain text using emojis.

Use this style:

🌍 Trip Overview

📅 Day 1

🌅 Morning
• Activity

🍽 Breakfast
• Restaurant/Food

🏛 Places to Visit
• Place 1
• Place 2

🍛 Lunch

🌇 Evening

🍽 Dinner

🏨 Stay

💰 Estimated Expense

Repeat the same format for every day.

After the itinerary, include:

🍴 Famous Local Foods

🛍 Shopping Recommendations

🎒 Packing Checklist

🛡 Safety Tips

💵 Money Saving Tips

🌦 Best Time to Visit

☎ Emergency Contacts
Police: 112
Ambulance: 108

Keep the language simple, attractive and user-friendly.

The response should look like a professional travel application, not a markdown document.
"""

    response = model.generate_content(prompt)

    return response.text