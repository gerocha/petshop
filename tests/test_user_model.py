from petshop.user_model import authenticate, get_user


def test_authenticate_existing_user_should_return_user(user_batima):
    auth = authenticate(username=user_batima['username'],
                        password=user_batima['password'])

    assert auth is not None


def test_is_correct_password_with_correct_password(user_batima):
    user = get_user('batima')

    assert user.is_correct_password('123456') == True
