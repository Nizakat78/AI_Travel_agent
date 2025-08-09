from agents import Agent
from agents import RunContextWrapper
import chainlit as cl

def make_on_handoff_message(agent: Agent):
    async def _on_handoff(ctx: RunContextWrapper[None]):
        await cl.Message(
            content=f"Handoff to {agent.name} initiated..."
        ).send()

        # ✅ Store the next agent in Chainlit's user session
        cl.user_session.set("agent", agent)

    return _on_handoff
