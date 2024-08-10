import random
from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordGenerator:
    """
    A class to generate a random password and its hashed version.
    :param length: The length of the password. Default is 3.
    :param lower_case: The lower case characters to be used in the password. Default is 'abcdefghijklmnopqrstuvwxyz'.
    :param upper_case: The upper case characters to be used in the password. Default is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.
    :param numbers: The numbers to be used in the password. Default is '0123456789'.
    """

    def __init__(self,
                 length: int = 3,
                 lower_case: str = 'abcdefghijklmnopqrstuvwxyz',
                 upper_case: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                 numbers: str = '0123456789'):
        self.length = length
        self.plain_password = None
        self.hash_password = None
        self.lower_case = lower_case
        self.upper_case = upper_case
        self.numbers = numbers

    def _generate_plain_password(self, length: int) -> str:
        """
        Generate a plain password with the specified length.
        :param length: The length of the password.
        :return: The plain password.
        """
        char_sets = [self.lower_case, self.upper_case, self.numbers]
        self.plain_password = '-'.join(
            ''.join(random.choice(char_set) for _ in range(length)) for char_set in char_sets)
        return self.plain_password

    def _generate_password_hash(self, password: str) -> str:
        """
        Generate a hashed password using bcrypt.
        :param password: The plain password.
        :return: The hashed password.
        """
        self.hash_password = PWD_CONTEXT.hash(password)
        return self.hash_password

    def generate_password(self) -> tuple[str, str]:
        """
        Generate a plain password and its hashed version.
        :return: A tuple containing the plain password and its hashed version.
        """
        plain_password = self._generate_plain_password(self.length)
        hash_password = self._generate_password_hash(plain_password)
        return plain_password, hash_password


class PasswordVerifier:
    """
    A class to verify a plain password against its hashed version.
    :param plain_password: The plain password to be verified.
    :param hash_password: The hashed password to be verified against.
    """

    def __init__(self, plain_password: str, hash_password: str):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.plain_password = plain_password
        self.hash_password = hash_password

    def verify_password(self) -> bool:
        """
        Verify the plain password against its hashed version.
        :return: True if the plain password matches the hashed password, False otherwise.
        """
        return self.pwd_context.verify(self.plain_password, self.hash_password)
