import pytest
import unittest

from server.src.models.models import db, User


@pytest.mark.usefixtures("app")
class TestValidateRequestBody(unittest.TestCase):
    def setUp(self):
        self.name = "Hamlet"
    
    def tearDown(self):
        with self.app.app_context():
            test_user = User.query.filter(User.name == self.name).first()
            if test_user:
                db.session.delete(test_user)
                db.session.commit()
    
    def test_no_body_abort(self):
        response = self.client.post("/user-data", json={})
        self.assertEqual(response.status_code, 400)
        
    def test_dict_mutable(self):
        with self.app.app_context():
            response = self.client.post("/user-data", json={"name": self.name, "age": "", "favoriteColor": "Orange"}) # accessing the test_client through self.client
            data = response.get_json()
            self.assertEqual(data["userCount"], 15)
        
        
        
    
    