from petshop.user_model import get_user, insert_user


def test_user_insert(client, app):
    payload = {
            'username': 'batima',
            'password': '123456',
            'email': 'teste@teste.com'
            }
    res = client.post('/user', data=payload)

    assert res.status_code == 201
    assert get_user(payload['username']) is not None


def test_user_insert_missing_param_should_not_create_user(client, app):
    res = client.post('/user', data={})
    assert len(res.json['error']) > 0
    assert res.status_code == 400
    res = client.post('/user', data={
        'username': 'batima'
        })
    assert len(res.json['error']) > 0
    assert res.status_code == 400


def test_insert_existing_user_should_location_to_existing_user(client, app):
    payload = {
            'username': 'batima',
            'password': 'batima123',
            'email': 'teste@teste.com'
            }
    insert_user(payload)
    res = client.post('/user', data=payload)
    assert res.status_code == 409
