from flask import json
from petshop.user_model import get_user


def test_login_with_right_credentials(user_batima, client):
    res = client.post('/auth', data=json.dumps(user_batima),
                      headers={'content-type': 'application/json'})

    print(get_user('batima').is_correct_password('123456'))

    assert res.status_code == 200
