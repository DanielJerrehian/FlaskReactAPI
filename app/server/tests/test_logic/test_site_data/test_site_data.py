import unittest

from src.app import create_app
from src.logic.site_data.site_data import SiteData


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

    def test_average_user_age(self):
        with self.app.app_context():
            site_data = SiteData()
            site_data.average_user_age()
            self.assertEqual(round(site_data.average_age, 0), 28)

    def test_fetch_last_three_users(self):
        with self.app.app_context():
            site_data = SiteData()
            site_data.fetch_last_three_users()
            print(site_data.test.to_dict())
            self.assertEqual(site_data.last_three_users[0]["name"], "Ruben")
            self.assertEqual(site_data.last_three_users[1]["name"], "Aurelien")
            self.assertEqual(site_data.last_three_users[2]["name"], "Cynthia")
            
    def tearDown(self):
        pass