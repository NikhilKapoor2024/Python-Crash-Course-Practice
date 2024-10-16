class AnonymousSurvey:
    """A class that represents a survey"""

    def __init__(self, question):
        """Stores a question and a list of responses"""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Shows a question"""
        print(self.question)
    
    def store_response(self, new_response):
        """Stores a response into the responses list"""
        self.responses.append(new_response)
    
    def show_results(self):
        """Shows all the responses in responses list"""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")