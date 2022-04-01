import unittest
import sys
import os

sys.path.append(os.path.join("app", "server"))

from app.server.src.app import create_app
from app.server.src.logic.site_data.site_data import SiteData


class TestSiteData(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
    
    def test_class_exists(self):
        site_data = SiteData
        self.assertTrue(site_data)
        
    def test_get_project_name(self):
        site_data = SiteData()
        site_data.get_project_name()
        self.assertEqual(site_data.project_name, "FlaskReactAPI")
        
    def test_count_user(self):
        with self.app.app_context():
            site_data = SiteData()
            site_data.count_user()
            self.assertEqual(site_data.user_count, 14)
            
    def test_get_favorite_color(self):
        with self.app.app_context():
            site_data = SiteData()
            site_data.get_favorite_color()
            self.assertEqual(site_data.favorite_color, "Purple")
            
    def tearDown(self):
        pass