from src.logic.site_data.site_data import SiteData

    
def test_class_exists():
    site_data = SiteData
    assert site_data

def test_class_vars():
    site_data = SiteData()
    assert site_data.project_name == None
    assert site_data.user_count == None
    assert site_data.favorite_color == None
    assert site_data.second_favorite_color == None
    assert site_data.average_age == None
    assert site_data.last_three_users == None
        
def test_get_project_name():
    site_data = SiteData()
    site_data.get_project_name()
    assert site_data.project_name == "FlaskReactAPI"
        
def test_count_user(app):
    with app.app_context():
        site_data = SiteData()
        site_data.count_user()
        assert site_data.user_count == 14
            
def test_get_favorite_color(app):
    with app.app_context():
        site_data = SiteData()
        site_data.get_favorite_color()
        assert site_data.favorite_color == "Purple"

def test_get_favorite_color(app):
    with app.app_context():
        site_data = SiteData()
        site_data.get_second_favorite_color()
        assert site_data.second_favorite_color == "Red"

def test_average_user_age(app):
    with app.app_context():
        site_data = SiteData()
        site_data.average_user_age()
        assert round(site_data.average_age, 0) == 28

def test_fetch_last_three_users(app):
    with app.app_context():
        site_data = SiteData()
        site_data.fetch_last_three_users()
        assert site_data.last_three_users[0].name == "Ruben"
        assert site_data.last_three_users[1].name == "Aurelien"
        assert site_data.last_three_users[2].name == "Cynthia"