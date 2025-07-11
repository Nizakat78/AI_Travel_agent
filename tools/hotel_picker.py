# tools/hotel_picker.py
# from openai.agents import tool # Hypothetical decorator

# @tool
def pick_hotel(hotel_option: str) -> str:
    """
    Simulates picking a specific hotel option.
    In a real scenario, this might involve more complex selection criteria or a booking confirmation.
    """
    if "Luxury" in hotel_option:
        return f"Booking confirmed for the Luxury option: {hotel_option}. Enjoy your stay!"
    elif "Boutique" in hotel_option:
        return f"Booking confirmed for the Boutique option: {hotel_option}. Enjoy your stay!"
    else:
        return f"You've selected: {hotel_option}. This is a mock confirmation."