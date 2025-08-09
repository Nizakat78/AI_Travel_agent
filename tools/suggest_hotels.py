from agents import function_tool, RunContextWrapper
from typing import TypedDict

class HotelSearchInput(TypedDict):
    destination: str

class HotelSearchOutput(TypedDict):
    hotels: str  # ❌ No Optional or Union

@function_tool
async def suggest_hotels(wrapper: RunContextWrapper, input: HotelSearchInput) -> HotelSearchOutput:
    destination = input["destination"].strip()
    hotels_data = f"""
[TOOL: suggest_hotels] 🏨 Hotel recommendations for {destination}:

1. Grand Palace Hotel - ★★★★★ - $200/night - Luxury stay with city view.
2. Cozy Inn - ★★★★ - $90/night - Family-friendly with breakfast included.
3. Budget Lodge - ★★★ - $50/night - Affordable stay, basic amenities.
"""
    return {"hotels": hotels_data}
