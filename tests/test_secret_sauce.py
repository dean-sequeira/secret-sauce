from src.secret_sauce import PasswordGenerator, PasswordVerifier


def test_generate_password():
    plain_password, hash_password = PasswordGenerator(length=3).generate_password()
    # Check if plain password is correctly formatted
    assert len(plain_password.split('-')) == 3

    # Check if each part of the plain password has the correct length
    assert all(len(part) == 3 for part in plain_password.split('-'))

    # Check if hash password is generated
    assert hash_password is not None


def test_verify_password():
    plain_password, hash_password = PasswordGenerator(length=3).generate_password()

    # Check if the plain password matches the hashed password
    assert PasswordVerifier(plain_password, hash_password).verify_password()

    # Check if an incorrect password does not match the hashed password
    assert not PasswordVerifier("wrong-password", hash_password).verify_password()
