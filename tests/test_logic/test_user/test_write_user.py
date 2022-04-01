import unittest 
import sys
import os

sys.path.append(os.path.join("app", "server"))

from app.server.src.app import create_app
from app.server.src.models.models import db, User
from app.server.src.logic.user.write_user import WriteUser



class TestSiteData(unittest.TestCase):
    def setUp(self):
        self.name = "Test-User"
        self.age = 75
        self.favorite_color = "Purple"
    
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
        app = create_app()
        with app.app_context():
            write_user = WriteUser(name=self.name, age=self.age, favorite_color=self.favorite_color)
            write_user.write_user()
            written_user = User.query.filter(User.name == self.name).first()
            self.assertEqual(written_user.age, self.age)
            
    def tearDown(self):
        app = create_app()
        with app.app_context():
            test_user = User.query.filter(User.name == self.name).first()
            if test_user:
                db.session.delete(test_user)
                db.session.commit()
            