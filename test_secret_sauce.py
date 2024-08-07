# test_main.py
from secret_sauce import PasswordGenerator, verify_password


def test_generate_password():
    generator = PasswordGenerator(length=3)
    plain_password, hash_password = generator.generate_password()

    # Check if plain password is correctly formatted
    assert len(plain_password.split('-')) == 3
    assert all(len(part) == 3 for part in plain_password.split('-'))

    # Check if hash password is generated
    assert hash_password is not None


def test_verify_password():
    generator = PasswordGenerator(length=3)
    plain_password, hash_password = generator.generate_password()

    # Check if the plain password matches the hashed password
    assert verify_password(plain_password, hash_password)

    # Check if an incorrect password does not match the hashed password
    assert not verify_password("wrong-password", hash_password)
