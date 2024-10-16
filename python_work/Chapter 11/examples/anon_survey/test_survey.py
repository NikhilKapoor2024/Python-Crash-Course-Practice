import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test class for AnonymousSurvey class"""

    def setUp(self):
        """
        Creates instance of AnonymousSurvey class for use in all tests
        """
        question = "What language do you speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        

    def test_store_single_response(self):
        """Tests storing a single response"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    
    def test_store_mulitple_responses(self):
        """Tests storing mulitple responses"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)



if __name__ == '__main__':
    unittest.main()