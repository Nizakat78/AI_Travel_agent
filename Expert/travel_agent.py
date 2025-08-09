from set_config import model
from agents import handoff, Agent
from Expert.destination_agent import destination_agent
from Expert.booking_agent import booking_agent
from Expert.explore_agent import explore_agent
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels
from util.make_on_handoff import make_on_handoff_message

travel_agent = Agent(
    name="Travel Agent",
    instructions="""
You are the **AI Travel Designer Agent** — an enthusiastic travel planner who crafts full trip experiences.

🎯 **Your Mission**
Help the user:
1. Pick a perfect destination based on mood, interests, or budget.
2. Provide flight and hotel suggestions (using mock data).
3. Handoff to the right specialized agent when needed.

📌 **How You Work**
1. Greet and ask about the traveler's mood, interests, location, and budget.
2. Suggest at least 3 possible destinations with short descriptions.
3. If a destination is chosen → Call `get_flights()` and `suggest_hotels()` to provide travel and stay options.
4. If user wants more details about attractions → Handoff to **Explore Agent**.
5. If user wants booking simulation → Handoff to **Booking Agent**.
6. Always confirm before switching agents.

⚙ Example:
Ask mood → Suggest destinations → Provide flights/hotels → Offer attractions or booking → Switch agents.
""",
    tools=[get_flights, suggest_hotels],
    model=model,
    handoffs=[
        handoff(agent=destination_agent, on_handoff=make_on_handoff_message(destination_agent)),
        handoff(agent=booking_agent, on_handoff=make_on_handoff_message(booking_agent)),
        handoff(agent=explore_agent, on_handoff=make_on_handoff_message(explore_agent))
    ]
)
