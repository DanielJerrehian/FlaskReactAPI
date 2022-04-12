from flask import Blueprint, request

from src.logic.user.write_user import WriteUser
from src.logic.site_data.site_data import SiteData
from src.models.pydantic_models import UserValidationSchema
from src.models.models import UserSchema
from src.logic.request.prepare_request import prepare_request


main = Blueprint("main", __name__)


@main.get("/user-data")
def user_count():
    site_data = SiteData()
    site_data.count_user()
    site_data.average_user_age()
    site_data.fetch_last_three_users()
    return {
        "userCount": site_data.user_count,
        "averageAge": round(site_data.average_age, 0),
        "lastThreeUsers": UserSchema().dump(site_data.last_three_users, many=True),
    }, 200


@main.get("/color-data")
def top_color():
    site_data = SiteData()
    site_data.get_favorite_color()
    site_data.get_second_favorite_color()
    return {
        "topFavoriteColor": site_data.favorite_color,
        "secondFavoriteColor": site_data.second_favorite_color,
    }, 200


@main.get("/site-data")
def site_data():
    site_data = SiteData()
    site_data.get_project_name()
    site_data.count_user()
    site_data.get_favorite_color()
    return {
        "projectName": site_data.project_name,
        "userCount": site_data.user_count,
        "topFavoriteColor": site_data.favorite_color,
    }, 200


@main.post("/user-data")
def user_data():
    req = prepare_request(request.json)  # make decorator in future
    user_model = UserValidationSchema(name=req["name"], age=req["age"], favorite_color=req["favoriteColor"])
    write_user = WriteUser(name=user_model.name, age=user_model.age, favorite_color=user_model.favorite_color)
    write_user.write_user()
    site_data = SiteData()
    site_data.get_project_name()
    site_data.count_user()
    site_data.get_favorite_color()
    return {
        "projectName": site_data.project_name,
        "userCount": site_data.user_count,
        "topFavoriteColor": site_data.favorite_color,
    }, 200
