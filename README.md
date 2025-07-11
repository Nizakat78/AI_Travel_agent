# AI Travel Designer Agent

## Project Description
The AI Travel Designer Agent plans a full travel experience by coordinating between specialized agents. It suggests destinations, simulates travel bookings, and recommends local attractions and food based on user mood or interests.

## How it Works
This system leverages the OpenAI Agent SDK + Runner to orchestrate interactions between specialized agents and tools.

1.  **Destination Suggestion**: The `DestinationAgent` suggests travel destinations based on the user's mood or interests.
2.  **Booking Simulation**: Once a destination is chosen, the `DestinationAgent` hands off to the `BookingAgent`. The `BookingAgent` then uses `get_flights()` and `suggest_hotels()` tools (with mock data) to simulate travel arrangements.
3.  **Exploration Guide**: After booking simulation, the `BookingAgent` hands off to the `ExploreAgent`. The `ExploreAgent` suggests local attractions and food unique to the chosen destination.

## Agents Involved
* **`DestinationAgent`**: Responsible for suggesting initial travel destinations.
* **`BookingAgent`**: Focuses on simulating flight and hotel bookings.
* **`ExploreAgent`**: Shares information about local attractions and food.

## Tools Utilized
* **`Travel Info Generator`**: A tool (containing `get_flights()` and `suggest_hotels()`) used by the `BookingAgent` to retrieve mock flight and hotel information.
* **`Hotel Picker`**: A tool (conceptual, could be merged or more complex) used by `BookingAgent` for hotel suggestions.

## Handoff Logic
Dynamic handoffs are managed between `DestinationAgent`, `BookingAgent`, and `ExploreAgent`. The `main.py` (runner) and agent classes orchestrate these transitions based on the user's progress and the information gathered.

## Setup and Installation
(Instructions on how to set up your Python environment, install dependencies, and configure the OpenAI Agent SDK)

```bash
# Example:
# git ai_travel_designer_agent
# cd ai_travel_designer_agent
# pip install -r requirements.txt
# export OPENAI_API_KEY="your_openai_api_key"