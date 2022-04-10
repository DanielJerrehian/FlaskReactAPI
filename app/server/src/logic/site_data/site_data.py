from sqlalchemy import desc, func

from src.models.models import db, User
from src.logic.model_to_json.row_to_dict import row_to_dict

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
        
    def average_user_age(self):
        self.average_age = db.session \
            .query(func.avg(User.age)) \
            .filter(User.age != None) \
            .scalar()

    def fetch_last_three_users(self):
        last_three_users = User.query \
            .order_by(User.id.desc()) \
            .limit(3) \
            .all()
        
        self.test = last_three_users

        self.last_three_users = []
        for row_object in last_three_users:
            row = row_to_dict(row_object)
            self.last_three_users.append(row)

        # print(self.last_three_users)
