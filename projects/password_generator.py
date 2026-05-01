
import secrets  # to generate cryptographically secure numbers
import string  # to generate a bunch of string, because it is annoying to ype 'some  string' like this


class SecurePasswordGenerator:
    """
    Now we are going to be building password generator. for this we use secretes module, that use to generate random
    information such as numbers in a secure way. never use random module, that should be cryptographically secure.

    Args:
        length:abs(int)

    Returns:
        string of uppercase, lowercase, digits and punctuation characters

    Example:
        secure_password = SecurePasswordGenerator(length=56) \n
        print(secure_password.generate_password())
    """
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = abs(int(length))
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # get characters from the string module
        self.base_characters: str = string.ascii_lowercase + string.digits  # 'abcdefghijklmnopqrstuvwxyz'  # '0123456789'
        self.base_uppercase: str = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.base_punctuation: str = string.punctuation  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate_password(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return "".join(password)


def main() -> None:
    try:
        user_input: str = input("Please enter the password length: ")
        converted_password_length = abs(int(user_input))
        secure_password: SecurePasswordGenerator = SecurePasswordGenerator(length=converted_password_length)
        print(secure_password.generate_password())
    except ValueError as ve:
        print(f"please enter integer value. ", ve)


if __name__ == '__main__':
    main()
"""
Homework:

1. Create a method in the Password class which checks the passwords strength.
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols
"""
