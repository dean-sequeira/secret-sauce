# Secret Sauce

## Overview

Secret Sauce is a Python-based password generator that returns both plain text and hashed results. It uses the `passlib`
library with bcrypt for hashing passwords, ensuring secure password storage and verification.

## Features

- Generates a plain text password with a customizable length.
- Hashes the generated plain text password using bcrypt.
- Verifies plain text passwords against their hashed versions.

## Requirements

- Python 3.11
- `passlib[bcrypt]` version 1.7.4
- `bcrypt` version 4.0.1
- `pytest` for running tests

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd secret-sauce
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Import the `PasswordGenerator` class and `verify_password` function from `secret_sauce.py`:
    ```python
    from secret_sauce import PasswordGenerator, verify_password
    ```

2. Generate a password:
    ```python
    generator = PasswordGenerator(length=3)
    plain_password, hash_password = generator.generate_password()
    print(f"Plain Password: {plain_password}")
    print(f"Hashed Password: {hash_password}")
    ```

3. Verify a password:
    ```python
    is_valid = verify_password(plain_password, hash_password)
    print(f"Password is valid: {is_valid}")
    ```

## Running Tests

1. Save the test code in a file named `test_secret_sauce.py`.
2. Run the tests using `pytest`:
    ```sh
    pytest test_secret_sauce.py
    ```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.