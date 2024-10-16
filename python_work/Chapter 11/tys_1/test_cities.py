import unittest
from city_functions import get_full_location

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Test for 'City, Country' inputs (ex: 'Santiago, Chile')"""
        formatted_location = get_full_location('santiago', 'chile')
        self.assertEqual(formatted_location, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Test for 'City, Country - population XXXX' inputs"""
        formatted_location = get_full_location('santiago', 'chile', 500000000)
        self.assertEqual(formatted_location, 'Santiago, Chile - population=500000000')
    
if __name__ == '__main__':
    unittest.main()
