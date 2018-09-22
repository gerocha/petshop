from flask import jsonify

def test_insert_pet_should_insert(client, logged_batima):
    payload = {
            'name': 'fofinho',
            'type': 'dog',
            }

    res = client.post('/pet', data=payload,
            headers={'AUTHORIZATION': logged_batima})

    assert res.status_code == 201
