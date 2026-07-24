from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf(
    filename,
    source,
    destination,
    days,
    travelers,
    transport,
    hotel_type,
    budget,
    prediction,
    itinerary,
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Travel Planner</b>", styles["Title"]))
    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph(f"<b>Source:</b> {source}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Destination:</b> {destination}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Days:</b> {days}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Travelers:</b> {travelers}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Transport:</b> {transport}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Hotel Type:</b> {hotel_type}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Budget:</b> ₹{budget}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Predicted Expense:</b> ₹{prediction}", styles["BodyText"]))

    story.append(Paragraph("<br/>", styles["Normal"]))

    story.append(Paragraph("<b>AI Itinerary</b>", styles["Heading2"]))

    itinerary = itinerary.replace("\n", "<br/>")

    story.append(Paragraph(itinerary, styles["BodyText"]))

    doc.build(story)