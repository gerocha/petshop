def test_insert_pet_should_insert(client, logged_batima):
    payload = {
            'name': 'fofinho',
            'type': 'dog',
            }

    access_token = 'JWT ' + logged_batima.json['access_token']
    res = client.post('/pet',
                      data=payload,
                      headers={
                          'AUTHORIZATION': access_token
                          })

    assert res.status_code == 201
