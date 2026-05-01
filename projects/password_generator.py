"""
Now we are going to be building password generator. for this we use secretes module, that use to generate random
information such as numbers in a secure way. never use random module, that should be cryptographically secure.
"""
import secrets  # to generate cryptographically secure numbers
import string  # to generate a bunch of string, because it is annoying to ype 'some  string' like this


class SecurePasswordGenerator:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        # get characters from the string module
        self.base_characters: str = string.ascii_lowercase + string.digits
        self.base_uppercase: str = string.ascii_uppercase
        self.base_punctuation: str = string.punctuation

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
    secure_password: SecurePasswordGenerator = SecurePasswordGenerator(length=56)
    print(secure_password.generate_password())


if __name__ == '__main__':
    main()
"""
Homework:

1. Create a method in the Password class which checks the passwords strength.
- check that the password is more than 16 characters long
- check that the password both contains uppercase characters and symbols
"""
