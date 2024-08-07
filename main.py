import random
from passlib.context import CryptContext

# Constants
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordGenerator:
    def __init__(self, length: int = 3):
        """
        Initialize the PasswordGenerator with a specified length.
        """
        self.length = length
        self.plain_password = None
        self.hash_password = None

    def _generate_plain_password(self, length: int) -> str:
        """
        Generate a plain password with the specified length.
        """
        char_sets = [LOWER_LETTERS, UPPER_LETTERS, NUMBERS]
        self.plain_password = '-'.join(
            ''.join(random.choice(char_set) for _ in range(length)) for char_set in char_sets)
        return self.plain_password

    def _generate_password_hash(self, password: str) -> str:
        """
        Generate a hashed password using bcrypt.
        """
        self.hash_password = PWD_CONTEXT.hash(password)
        return self.hash_password

    def generate_password(self) -> tuple[str, str]:
        """
        Generate a plain password and its hashed version.
        """
        plain_password = self._generate_plain_password(self.length)
        hash_password = self._generate_password_hash(plain_password)
        return plain_password, hash_password


def verify_password(plain_password, hash_password) -> bool:
    """
    Verify the plain password against its hashed version.
    """
    return PWD_CONTEXT.verify(plain_password, hash_password)
