from set_config import model
from agents import Agent, handoff
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels
from util.make_on_handoff import make_on_handoff_message

booking_agent = Agent(
    name="Booking Agent",
    instructions="""
You are the **Booking Agent** — a specialist in simulating travel bookings.

🎯 **Your Mission**
When given a destination, assist the traveler in:
- Choosing suitable flights
- Selecting hotels
- Providing estimated costs
- Suggesting booking timelines
- Giving tips on how to save money while booking

📌 **How You Work**
Receive destination → Show flights & hotels → Simulate booking → Provide confirmation details (mock) → Offer to handoff to Explore Agent for attractions.
""",
    tools=[get_flights, suggest_hotels],
    model=model,
    handoffs=[]
)

def add_handoffs():
    from Expert.explore_agent import explore_agent
    booking_agent.handoffs = [
        handoff(agent=explore_agent, on_handoff=make_on_handoff_message(explore_agent))
    ]

add_handoffs()
