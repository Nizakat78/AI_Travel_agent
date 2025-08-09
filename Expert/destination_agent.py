from set_config import model
from agents import Agent, handoff
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels
from util.make_on_handoff import make_on_handoff_message

destination_agent = Agent(
    name="Destination Agent",
    instructions="""
You are the **Destination Agent** — an expert in suggesting travel destinations.

🎯 **Your Mission**
When the traveler shares mood/interests:
- Suggest at least 3 destinations with short reasons.
- Mention season/weather tips if relevant.
- Offer to show flights & hotels (using tools).

📌 **How You Work**
Receive mood/interests → Suggest destinations → Offer travel/hotel info → Ask if they want booking or attractions → Handoff accordingly.
""",
    tools=[get_flights, suggest_hotels],
    model=model,
    handoffs=[]
)

def add_handoffs():
    from Expert.booking_agent import booking_agent
    from Expert.explore_agent import explore_agent
    destination_agent.handoffs = [
        handoff(agent=booking_agent, on_handoff=make_on_handoff_message(booking_agent)),
        handoff(agent=explore_agent, on_handoff=make_on_handoff_message(explore_agent))
    ]

add_handoffs()
