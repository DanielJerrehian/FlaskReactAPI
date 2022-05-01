import pytest
import unittest

from src.models.models import db, User

@pytest.mark.usefixtures("app") # "bridge" the below unittest class with the function "app" in conftest.py, giving access to self.app and self.client inexplicitly
class TestIndex(unittest.TestCase):
    def setUp(self):
        """"
        Although not necessary (since the above decorator automatically instantiates them) it may improve readability 
        to explicitly instantiate the app and client here by doing:
        
        self.app = self.app 
        self.client = self.client
        """
        self.name = "Test-User"
        self.age = 75
        self.favorite_color = "Purple"
        self.json_data = {
            "name": self.name,
            "age": self.age,
            "favoriteColor": self.favorite_color
        }
        
    def tearDown(self):
        """
        Here the app_context is accessed simply by writing self.app.app_context, since pytest created the app (self.app) for us to use throughout the entire class
        """
        with self.app.app_context():
            test_user = User.query.filter(User.name == self.name).first()
            if test_user:
                db.session.delete(test_user)
                db.session.commit()
                
    def test_get_user_data(self):
        response = self.client.get("/user-data") # accessing the test_client through self.client
        data = response.get_json() 
        self.assertEqual(data["userCount"], 14)
        self.assertEqual(round(data["averageAge"], 0), 28)
        self.assertEqual(data["lastThreeUsers"][0]["name"], "Ruben")
        self.assertEqual(response.status_code, 200)
            
    def test_get_top_color(self):
        response = self.client.get("/color-data") # accessing the test_client through self.client
        data = response.get_json()
        self.assertEqual(data["topFavoriteColor"], "Purple")
        self.assertEqual(data["secondFavoriteColor"], "Red")
        self.assertEqual(response.status_code, 200)            

    def test_get_site_data(self):
        response = self.client.get("/site-data") # accessing the test_client through self.client
        data = response.get_json()
        self.assertEqual(data["projectName"], "FlaskReactAPI")
        self.assertEqual(data["userCount"], 14)
        self.assertEqual(data["topFavoriteColor"], "Purple")
        self.assertEqual(response.status_code, 200)
            
    def test_post_user_data(self):
        with self.app.app_context(): # need app context since this is a DB operation and the DB is not initialized without creating the app
            response = self.client.post("/user-data", json=self.json_data) # accessing the test_client through self.client
            data = response.get_json()
            written_user = User.query.filter(User.name == self.name).first()
            self.assertEqual(written_user.age, self.age)
            self.assertEqual(data["projectName"], "FlaskReactAPI")
            self.assertEqual(data["userCount"], 15)
            self.assertEqual(data["topFavoriteColor"], "Purple")
            self.assertEqual(response.status_code, 200)
            