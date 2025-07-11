# agents/explore_agent.py
# from openai.agents import Agent # Hypothetical SDK base class

class ExploreAgent:
    def __init__(self):
        self.name = "ExploreAgent"
        self.destination_context = None
        self.explore_data = {
            "Maldives": {
                "attractions": ["Bikini Beach", "Male Fish Market", "National Museum"],
                "food": ["Garudhiya (fish broth)", "Mas Huni (shredded fish)", "Bis Keemiya (samosa-like)"]
            },
            "Bali": {
                "attractions": ["Ubud Monkey Forest", "Tanah Lot Temple", "Mount Batur"],
                "food": ["Nasi Goreng", "Babi Guling", "Mie Goreng"]
            },
            "Phuket": {
                "attractions": ["Patong Beach", "Big Buddha", "Old Phuket Town"],
                "food": ["Pad Thai", "Tom Yum Goong", "Massaman Curry"]
            },
            # Add more mock data for other destinations as needed
        }

    def process_query(self, query: str, tools: dict, context: dict) -> tuple[str, str, dict]:
        context_update = {}
        self.destination_context = context.get("destination_for_explore")

        if not self.destination_context:
            return "I need a destination to provide exploration info. Please specify.", self.name, context_update

        destination_info = self.explore_data.get(self.destination_context)

        if destination_info:
            attractions = ", ".join(destination_info.get("attractions", ["No attractions found."]))
            food = ", ".join(destination_info.get("food", ["No local food found."]))
            response = (
                f"For {self.destination_context}, here are some popular spots and local foods:\n"
                f"Attractions: {attractions}\n"
                f"Local Food: {food}\n"
                f"Enjoy your trip!"
            )
            return response, self.name, context_update # Stay or signal completion
        else:
            return f"I don't have detailed exploration info for {self.destination_context} yet.", self.name, context_update