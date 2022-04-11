import unittest

from src.app import create_app
from src.models.models import db, User


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        self.name = "Test-User"
        self.age = 75
        self.favorite_color = "Purple"
        self.json_data = {
            "name": self.name,
            "age": self.age,
            "favoriteColor": self.favorite_color
        }
        
    def test_get_user_data(self):
        with self.app.test_client() as client:
            response = client.get("/user-data")
            data = response.get_json()
            self.assertEqual(data["userCount"], 14)
            self.assertEqual(round(data["averageAge"], 0), 28)
            self.assertEqual(data["lastThreeUsers"][0]["name"], "Ruben")
            
            self.assertEqual(response.status_code, 200)
            
    def test_get_top_color(self):
        with self.app.test_client() as client:
            response = client.get("/color-data")
            data = response.get_json()
            self.assertEqual(data["topFavoriteColor"], "Purple")
            self.assertEqual(data["secondFavoriteColor"], "Red")
            self.assertEqual(response.status_code, 200)            

    def test_get_site_data(self):
        with self.app.test_client() as client:
            response = client.get("/site-data")
            data = response.get_json()
            self.assertEqual(data["projectName"], "FlaskReactAPI")
            self.assertEqual(data["userCount"], 14)
            self.assertEqual(data["topFavoriteColor"], "Purple")
            self.assertEqual(response.status_code, 200)
            
    def test_post_user_data(self):
        with self.app.test_client() as client:
            response = client.post("/user-data", json=self.json_data)
            data = response.get_json()
            written_user = User.query.filter(User.name == self.name).first()
            self.assertEqual(written_user.age, self.age)
            self.assertEqual(data["projectName"], "FlaskReactAPI")
            self.assertEqual(data["userCount"], 15)
            self.assertEqual(data["topFavoriteColor"], "Purple")
            
    def tearDown(self):
        app = create_app()
        with app.app_context():
            test_user = User.query.filter(User.name == self.name).first()
            if test_user:
                db.session.delete(test_user)
                db.session.commit()
            