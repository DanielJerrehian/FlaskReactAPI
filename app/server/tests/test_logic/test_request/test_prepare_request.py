import unittest

from server.src.logic.request.replace_empty_strings_with_none import replace_empty_strings_with_none


class TestPrepareRequest(unittest.TestCase):
    def setUp(self):
        self.request_no_empty_string_vals = {
            "name": "Charles",
            "age": 75,
            "favorite_sports_team": "Philadelphia Eagles"
        }
        self.request_with_empty_string_vals = {
            "name": "Charles",
            "age": "",
            "favorite_sports_team": "Philadelphia Eagles"
        }
    
    def test_func_exists(self):
        self.assertTrue(replace_empty_strings_with_none)
        
    def test_func_no_empty_string_vals(self):
        req = replace_empty_strings_with_none(self.request_no_empty_string_vals)
        self.assertEqual(
            req, 
            {
                "name": "Charles",
                "age": 75,
                "favorite_sports_team": "Philadelphia Eagles"
            }                   
        )
        
    def test_func_with_empty_string_vals(self):
        req = replace_empty_strings_with_none(self.request_with_empty_string_vals)
        self.assertEqual(
            req, 
            {
                "name": "Charles",
                "age": None,
                "favorite_sports_team": "Philadelphia Eagles"
            }                   
        )
        
    def tearDown(self):
        pass