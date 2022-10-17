import take_home
import pytest

def app():
    app = take_home.app
    yield app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
