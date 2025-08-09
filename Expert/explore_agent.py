from set_config import model
from agents import Agent, handoff
from tools.suggest_hotels import suggest_hotels
from util.make_on_handoff import make_on_handoff_message

explore_agent = Agent(
    name="Explore Agent",
    instructions="""
You are the **Explore Agent** — an expert in finding local attractions, activities, and food recommendations.

🎯 **Your Mission**
When given a destination:
- Suggest at least 3 top attractions
- Recommend local food experiences
- Give cultural tips and best visiting times
- Suggest nearby unique experiences (hidden gems)

📌 **How You Work**
Receive destination → Share attractions & food → Provide short travel tips → Offer to handoff to Booking Agent if traveler wants to confirm plans.
""",
    tools=[],
    model=model,
    handoffs=[]
)

def add_handoffs():
    from Expert.booking_agent import booking_agent
    explore_agent.handoffs = [
        handoff(agent=booking_agent, on_handoff=make_on_handoff_message(booking_agent))
    ]

add_handoffs()
