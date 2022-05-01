import pytest

from src.app import create_app


@pytest.fixture() # create pytest fixture for tests that require the app, app_context, or test_client
def app(request): # function that is callable by unittest classes - read more here: https://docs.pytest.org/en/latest/how-to/unittest.html#mixing-fixtures
    app = create_app() # create app through application factory found in app.py
    app.config.update({
        "TESTING": True, # set config for app testing
    })

    client = app.test_client() # set up the test_client to write tests for routers

    request.cls.app = app # allows the app to be accessible in unittest classes decorated with '@pytest.mark.usefixtures("app")' through self.app
    request.cls.client = client # allows the app test_client() to be accessible in unittest classes decorated with '@pytest.mark.usefixtures("app")' through self.client
        
