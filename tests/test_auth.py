from flask import json


def test_login_with_right_credentials(user_batima, client):
    res = client.post('/auth',
                      data=json.dumps({
                          'username': user_batima['username'],
                          'password': user_batima['password']
                          }),
                      headers={'content-type': 'application/json'})
    assert res.status_code == 200
