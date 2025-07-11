# agents/destination_agent.py
# from openai.agents import Agent # Hypothetical SDK base class

class DestinationAgent:
    def __init__(self):
        self.name = "DestinationAgent"
        self.mood_destinations = {
            "relaxing beach": ["Maldives", "Bali", "Phuket"],
            "adventure": ["New Zealand", "Patagonia", "Nepal"],
            "city break": ["Paris", "Tokyo", "New York"],
            "historical": ["Rome", "Athens", "Cairo"],
            "nature": ["Switzerland", "Canada", "Norway"],
        }
        self.suggested_destinations_from_last_turn = []
        self.chosen_destination = None

    def process_query(self, query: str, tools: dict, context: dict) -> tuple[str, str, dict]:
        query_lower = query.lower()
        found_moods = []
        current_suggestions = []
        context_update = {}

        # Step 1: Identify trip mood/interests and suggest destinations
        for mood, destinations in self.mood_destinations.items():
            if mood in query_lower:
                found_moods.append(mood)
                current_suggestions.extend(destinations)

        if found_moods:
            unique_suggestions = list(set(current_suggestions))
            self.suggested_destinations_from_last_turn = unique_suggestions
            response = f"Based on your desire for {', '.join(found_moods)} trip, I recommend destinations like {', '.join(unique_suggestions)}. Which one sounds good to you?"
            return response, self.name, context_update # Stay in DestinationAgent
        else:
            # Step 2: If no new mood/interests, check if the user is choosing from previous suggestions
            if self.suggested_destinations_from_last_turn:
                for dest in self.suggested_destinations_from_last_turn:
                    if dest.lower() in query_lower:
                        self.chosen_destination = dest
                        context_update["chosen_destination"] = dest # Update context for next agent
                        self.suggested_destinations_from_last_turn = [] # Clear suggestions
                        response = f"Excellent choice! Let's plan your trip to {dest}. Initiating booking simulation..."
                        return response, "BookingAgent", context_update # Handoff to BookingAgent
            # Fallback
            return "I'm not sure about that. What kind of trip are you looking for? (e.g., 'relaxing beach', 'adventure')", self.name, context_update