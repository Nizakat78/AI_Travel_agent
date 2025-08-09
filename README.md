# AI Travel Designer Agent — README

> **Project:** AI Travel Designer Agent  
> **Purpose:** A multi-agent Chainlit app that plans travel experiences by coordinating Destination, Booking, and Explore agents with mock flight & hotel tools.  
> **Pattern:** Follows the same multi-agent / tool / handoff architecture as the Career Mentor assignment.

---

## Table of contents
1. Project overview  
2. Folder structure (expected)  
3. Prerequisites  
4. Environment variables (`.env`)  
5. Install & run (local dev)  
6. How it works (agents, tools, handoffs)  
7. **Sample conversation** (ready to test)  
8. Troubleshooting & common fixes  
9. Submission checklist & demo tips

---

# 1. Project overview

This repository demonstrates a small multi-agent system using the OpenAI Agent SDK + Runner pattern and Chainlit for chat UI.  
Main features:

- `Travel Agent` coordinates the flow and suggests destinations.  
- `Destination Agent` recommends places and can call tools.  
- `Booking Agent` simulates booking flow.  
- `Explore Agent` suggests attractions, food, and local tips.  
- Tools: `get_flights()` and `suggest_hotels()` — return **mock data** so you can demo without real provider accounts (but the code supports real API calls if you configure them).  
- Hand-offs: Agents can hand off the session to one another; an on-handoff helper displays a short message and sets the next agent in Chainlit's user session.

---

# 2. Folder structure (expected)

# AI Travel Designer Agent — README

> **Project:** AI Travel Designer Agent  
> **Purpose:** A multi-agent Chainlit app that plans travel experiences by coordinating Destination, Booking, and Explore agents with mock flight & hotel tools.  
> **Pattern:** Follows the same multi-agent / tool / handoff architecture as the Career Mentor assignment.

---

## Table of contents
1. Project overview  
2. Folder structure (expected)  
3. Prerequisites  
4. Environment variables (`.env`)  
5. Install & run (local dev)  
6. How it works (agents, tools, handoffs)  
7. **Sample conversation** (ready to test)  
8. Troubleshooting & common fixes  
9. Submission checklist & demo tips

---

# 1. Project overview

This repository demonstrates a small multi-agent system using the OpenAI Agent SDK + Runner pattern and Chainlit for chat UI.  
Main features:

- `Travel Agent` coordinates the flow and suggests destinations.  
- `Destination Agent` recommends places and can call tools.  
- `Booking Agent` simulates booking flow.  
- `Explore Agent` suggests attractions, food, and local tips.  
- Tools: `get_flights()` and `suggest_hotels()` — return **mock data** so you can demo without real provider accounts (but the code supports real API calls if you configure them).  
- Hand-offs: Agents can hand off the session to one another; an on-handoff helper displays a short message and sets the next agent in Chainlit's user session.

---

# 2. Folder structure (expected)



AI_Travel_Agent/
├─ Expert/
│ ├─ travel_agent.py
│ ├─ destination_agent.py
│ ├─ booking_agent.py
│ ├─ explore_agent.py
├─ tools/
│ ├─ get_flights.py
│ ├─ suggest_hotels.py
├─ util/
│ ├─ make_on_handoff.py
├─ main.py
├─ set_config.py
├─ .env
├─ README.md <-- (this file)
└─ requirements.txt



---

# 3. Prerequisites

- Python **3.10+** (recommended).  
- `pip` (for installing packages).  
- Chainlit installed (we run the app via `chainlit run`).  
- Access to an LLM provider if you want real model calls (the code uses a Gemini-style config by default). For demo, mock tools are already included.

---

# 4. Environment variables (`.env`)



---

# 5. Install & runss
```bash
pip install -r requirements.txt
chainlit run main.py



```
# 7. Sample conversation
```
You can copy-paste these messages into the Chainlit chat to see the agent in action.

User:

Hi! I want to plan a trip.




Agent:

Greets and asks for your mood, interests, location, and budget.

User:

rust
Copy
Edit
I'm feeling adventurous, love mountains, budget around $800.
Agent:

Suggests at least 3 destinations (e.g., Denver, Asheville, Banff) with short descriptions.

User:

css
Copy
Edit
I like Kathmandu, Nepal.
Agent:

Calls get_flights() and suggest_hotels() tools, shows mock flights & hotels for Kathmandu.

User:

css
Copy
Edit
What can I explore there?
Agent:

Hands off to Explore Agent, shows top attractions, local food, cultural tips, and hidden gems.

User:

kotlin
Copy
Edit
Can you book this trip for me?
Agent:

Hands off to Booking Agent, simulates booking, provides mock confirmation, and cost breakdown.

User:

css
Copy
Edit
I want to go to Paris. Show me flights and hotels.
Agent:

Directly returns mock flight and hotel listings for Paris.