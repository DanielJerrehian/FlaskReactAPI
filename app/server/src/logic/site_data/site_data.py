from src.app import db
from src.models.models import User


class SiteData():
    def __init__(self):
        self.user_count = None
        self.favorite_color = None
        
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
        