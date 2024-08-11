import random

class VrindaAI:
    def __init__(self):
        self.responses = {
            "What is 2 + 2?": "4",
            "What is the capital of France?": "Paris",
            "Explain machine learning.": "Machine learning is a branch of AI that allows systems to learn and improve from experience without being explicitly programmed.",
        }

    def get_response(self, user_input):
        return self.responses.get(user_input, "I'm not sure about that.")
