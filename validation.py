class ResponseValidator:
    def __init__(self):
        self.correct_answers = {
            "What is 2 + 2?": "4",
            "What is the capital of France?": "Paris",
            "Explain machine learning.": "Machine learning is a branch of AI that allows systems to learn and improve from experience without being explicitly programmed.",
        }

    def validate_response(self, user_input, ai_response):
        expected_response = self.correct_answers.get(user_input)
        return expected_response == ai_response
