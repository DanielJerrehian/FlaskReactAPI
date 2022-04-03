import unittest
import sys
import os

from src.logic.request.prepare_request import prepare_request

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
        self.assertTrue(prepare_request)
        
    def test_func_no_empty_string_vals(self):
        req = prepare_request(self.request_no_empty_string_vals)
        self.assertEqual(
            req, 
            {
                "name": "Charles",
                "age": 75,
                "favorite_sports_team": "Philadelphia Eagles"
            }                   
        )
        
    def test_func_with_empty_string_vals(self):
        req = prepare_request(self.request_with_empty_string_vals)
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