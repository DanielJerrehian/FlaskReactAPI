from sqlalchemy import func

from server.src.models.models import db, User


class SiteData():
    def __init__(self):
        self.project_name = None
        self.user_count = None
        self.favorite_color = None
        self.second_favorite_color = None
        self.average_age = None
        self.last_three_users = None
        
    def get_project_name(self):
        self.project_name = "FlaskReactAPI"
        
    def count_user(self):
        self.user_count = User.query.count()
        
    def get_favorite_color(self):
        self.favorite_color = db.session \
            .query(User.favorite_color) \
            .filter(User.favorite_color != None) \
            .group_by(User.favorite_color) \
            .order_by(db.func.count(User.favorite_color).desc()) \
            .first() \
            .favorite_color
    
    def get_second_favorite_color(self):
        self.second_favorite_color = db.session \
            .query(User.favorite_color) \
            .filter(User.favorite_color != None) \
            .group_by(User.favorite_color) \
            .order_by(db.func.count(User.favorite_color).desc()) \
            .all() \
            [1] \
            .favorite_color
        
    def average_user_age(self):
        self.average_age = db.session \
            .query(func.avg(User.age)) \
            .filter(User.age != None) \
            .scalar()

    def fetch_last_three_users(self):
        self.last_three_users = User.query \
            .order_by(User.id.desc()) \
            .limit(3) \
            .all()