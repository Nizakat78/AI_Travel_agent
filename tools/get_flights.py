from agents import function_tool, RunContextWrapper
from typing import TypedDict

class FlightSearchInput(TypedDict):
    destination: str

class FlightSearchOutput(TypedDict):
    flights: str  # ❌ No Optional or Union

@function_tool
async def get_flights(wrapper: RunContextWrapper, input: FlightSearchInput) -> FlightSearchOutput:
    destination = input["destination"].strip()
    flights_data = f"""
[TOOL: get_flights] ✈️ Flight options for {destination}:

1. Economy Saver - $450 - Non-stop - Airline: SkyAir
2. Business Flex - $1200 - 1 Stop - Airline: LuxFly
3. Budget Air - $320 - 2 Stops - Airline: EconAir
"""
    return {"flights": flights_data}
