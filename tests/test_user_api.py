def test_user_insert(client, app):
    assert client.post('/user',
                       data={'username': 'batima'}).status_code == 201


def test_user_insert_missing_param_should_not_create_user(client, app):
    res = client.post('/user', data={})
    assert len(res.json['error']) > 0
    assert res.status_code == 400
