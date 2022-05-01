from server.src.models.models import db, User


class WriteUser():
    def __init__(self, name:str=None, age:int=None, favorite_color:str=None):
        self.name = name
        self.age = age
        self.favorite_color = favorite_color
        self.user = User(name=self.name, age=self.age, favorite_color=self.favorite_color)
        
    def write_user(self):
        db.session.add(self.user)
        db.session.commit()