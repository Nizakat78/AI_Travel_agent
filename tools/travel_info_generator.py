# tools/travel_info_generator.py
# from openai.agents import tool # Hypothetical decorator

# @tool
def get_flights(destination: str) -> str:
    """
    Simulates fetching flight details for a given destination.
    Returns mock flight information.
    """
    destination_lower = destination.lower()
    if "maldives" in destination_lower:
        return "Flight #123 from [Origin] to Male (MLE), Departure: 2025-08-10, Price: $800"
    elif "bali" in destination_lower:
        return "Flight #456 from [Origin] to Denpasar (DPS), Departure: 2025-08-15, Price: $700"
    elif "phuket" in destination_lower:
        return "Flight #789 from [Origin] to Phuket (HKT), Departure: 2025-08-20, Price: $650"
    else:
        return "No mock flight info available for this destination."

# @tool
def suggest_hotels(destination: str) -> str:
    """
    Simulates suggesting hotel options for a given destination.
    Returns mock hotel information.
    """
    destination_lower = destination.lower()
    if "maldives" in destination_lower:
        return "Luxury Resort (5-star, $500/night), Boutique Hotel (4-star, $250/night)"
    elif "bali" in destination_lower:
        return "Beachfront Villa (4.5-star, $300/night), Budget Guesthouse (3-star, $80/night)"
    elif "phuket" in destination_lower:
        return "Ocean View Hotel (4-star, $200/night), City Center Hostel (2-star, $50/night)"
    else:
        return "No mock hotel info available for this destination."