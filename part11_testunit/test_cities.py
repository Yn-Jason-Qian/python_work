import unittest
from city_functions import format_city

class CityFunctionsTest(unittest.TestCase):
    """ 测试city_functions.py """
    def test_format_city(self):
        formatted_city = format_city('beijing', 'china')
        self.assertEqual(formatted_city, 'Beijing, China')

    def test_city_country_population(self):
        formatted_city = format_city('beijing', 'china', 5000000)
        self.assertEqual(formatted_city, 'Beijing, China, Population = 5000000')
unittest.main()
