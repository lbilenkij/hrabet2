import unittest
from db_mock import TestDB
from Country import Country
class TestCountryObj(unittest.TestCase):
    def setUp(self):
        self.db = TestDB()
    def test_name(self):
        self.cntry = Country('ITA', self.db)
        self.assertEqual(self.cntry.name, 'Italy')