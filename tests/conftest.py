import os
import tempfile

import pytest
from petshop import create_app, db
from petshop.user_model import insert_user
from flask import json

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app(request):
    db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        db.drop_all()
        ctx.pop()

    request.addfinalizer(teardown)
    db.create_all()
    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def user_batima(app):
    payload = {
            'username': 'batima',
            'password': '123456',
            'email': 'teste@teste.com'
            }
    insert_user(payload)

    return payload


@pytest.fixture
def logged_batima(user_batima, client):
    res = client.post('/auth',
                      data=json.dumps({
                          'username': user_batima['username'],
                          'password': user_batima['password']
                          }),
                      headers={'content-type': 'application/json'})
    return res
