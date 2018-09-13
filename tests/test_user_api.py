from petshop.user_model import get_user


def test_user_insert(client, app):
    payload = {
            'username': 'batima',
            'email': 'teste@teste.com'
            }
    res = client.post('/user', data=payload)

    assert res.status_code == 201
    assert get_user(payload['username']) is not None


def test_user_insert_missing_param_should_not_create_user(client, app):
    res = client.post('/user', data={})
    assert len(res.json['error']) > 0
    assert res.status_code == 400
