import pytest
import unittest 

from server.src.models.models import db, User
from server.src.logic.user.write_user import WriteUser

@pytest.mark.usefixtures("app")
class TestSiteData(unittest.TestCase):
    def setUp(self):
        self.name = "Test-User"
        self.age = 75
        self.favorite_color = "Purple"
    
    def tearDown(self):
        with self.app.app_context():
            test_user = User.query.filter(User.name == self.name).first()
            if test_user:
                db.session.delete(test_user)
                db.session.commit()
                
    def test_class_exists(self):
        write_user = WriteUser
        self.assertTrue(write_user)
        
    def test_pass_args_to_class(self):
        write_user = WriteUser(name=self.name, age=self.age, favorite_color=self.favorite_color)
        self.assertEqual(write_user.name, self.name)
        self.assertEqual(write_user.age, self.age)
        self.assertEqual(write_user.favorite_color, self.favorite_color)
        self.assertTrue(write_user.user)
    
    def test_write_user(self):
        with self.app.app_context():
            write_user = WriteUser(name=self.name, age=self.age, favorite_color=self.favorite_color)
            write_user.write_user()
            written_user = User.query.filter(User.name == self.name).first()
            self.assertEqual(written_user.age, self.age)
            
            