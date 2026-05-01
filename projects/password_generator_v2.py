import secrets  # cryptographically secure random generation
import string  # pre-built character set constants


# --- Custom Exceptions ---

class NegativeLengthError(ValueError):
    """
    Raised when user provides a negative number as password length.
    Negative password length کوئی معنی نہیں رکھتی۔
    """
    pass


class ZeroLengthError(ValueError):
    """
    Raised when user provides zero as password length.
    Zero length کا password بے کار ہوتا ہے۔
    """
    pass


class MinimumLengthError(ValueError):
    """
    Raised when password length is less than allowed minimum.
    بہت چھوٹا password secure نہیں ہوتا۔
    """
    pass


# --- Main Class ---

class SecurePasswordGenerator:
    """
    Cryptographically secure password generator۔

    یہ class `secrets` module استعمال کرتی ہے جو OS-level entropy
    سے random values generate کرتا ہے — `random` module کے برعکس
    جو predictable ہوتا ہے اور passwords کے لیے unsafe ہے۔

    Args:
        length (int): Password minimum length must be 8
        use_uppercase (bool): include Capital letters Default: True
        use_symbols (bool): include Special characters Default: True

    Raises:
        NegativeLengthError: raises if length is <0
        ZeroLengthError: raises if length is 0
        MinimumLengthError: raises if length is less than minimum length
        TypeError: if no integer length is given

    Example:
        >>> gen = SecurePasswordGenerator(length=16)
        >>> password = gen.generate_password()
        >>> print(password)
        'aB$3kR!mXq@9pLz#'
    """

    # Minimum allowed password length — class level constant
    MINIMUM_LENGTH: int = 8

    def __init__(
            self,
            length: int = 12,
            use_uppercase: bool = True,
            use_symbols: bool = True,
    ) -> None:
        """
        it initializes the Password generator and validate settings

        Args:
            length (int): Password کتنے characters کا ہو۔
            use_uppercase (bool): Uppercase letters, included or not ?
            use_symbols (bool): Symbols/punctuation, included or not ?
        """
        # --- Input Validation ---
        self._validate_length(length)

        self.length: int = length
        self.use_uppercase: bool = use_uppercase
        self.use_symbols: bool = use_symbols

        # --- Character Pool بنانا ---
        # ہمیشہ lowercase + digits base میں ہوں گے
        self._character_pool: str = (
                string.ascii_lowercase + string.digits
        )

        # Optional character sets add کرنا
        if self.use_uppercase:
            self._character_pool += string.ascii_uppercase

        if self.use_symbols:
            self._character_pool += string.punctuation

    @staticmethod
    def _validate_length(length: int) -> None:
        """
        Password length کو validate کرتا ہے۔
        ہر ممکن غلط input کے لیے الگ error raise کرتا ہے۔

        Args:
            length (int): Validate کی جانے والی length۔

        Raises:
            TypeError: اگر length integer نہ ہو۔
            NegativeLengthError: اگر length منفی ہو۔
            ZeroLengthError: اگر length صفر ہو۔
            MinimumLengthError: اگر length minimum سے کم ہو۔
        """
        # Check 1: کیا integer ہے؟
        if not isinstance(length, int):
            raise TypeError(
                f"Password length must be in integer "
                f" You provide {type(length).__name__}'"
            )

        # Check 2: کیا negative ہے؟
        if length < 0:
            raise NegativeLengthError(
                f"Password length ({length}) can't be negative number. "
                f"Provide positive number"
            )

        # Check 3: کیا صفر ہے؟
        if length == 0:
            raise ZeroLengthError(
                "Password length can't be Zero "
                f"minimum {SecurePasswordGenerator.MINIMUM_LENGTH} provide۔"
            )

        # Check 4: کیا minimum سے کم ہے؟
        if length < SecurePasswordGenerator.MINIMUM_LENGTH:
            raise MinimumLengthError(
                f"Password length {length} is very short. "
                f"minimum should be {SecurePasswordGenerator.MINIMUM_LENGTH}"
            )

    def generate_password(self) -> str:
        """
        ایک cryptographically secure password generate کرتا ہے۔

        ہر character کے لیے `secrets.choice()` استعمال ہوتا ہے جو
        `random.choice()` سے مختلف اور زیادہ secure ہے۔

        Returns:
            str: Randomly generated secure password۔

        Example:
            >>> gen = SecurePasswordGenerator(length=12)
            >>> gen.generate_password()
            'x7$Kp!mR2@nL'
        """
        # List comprehension سے password بنانا — loop سے تیز
        password: list[str] = [
            secrets.choice(self._character_pool)
            for _ in range(self.length)  # _ مطلب variable چاہیے نہیں
        ]

        return "".join(password)

    def __repr__(self) -> str:
        """readable representation of Object۔"""
        return (
            f"SecurePasswordGenerator("
            f"length={self.length}, "
            f"use_uppercase={self.use_uppercase}, "
            f"use_symbols={self.use_symbols})"
        )


# --- Helper Function for Input Parsing ---

def parse_password_length(raw_input: str) -> int:
    """
    User کی raw string input کو validate کرکے integer میں convert کرتا ہے۔

    Args:
        raw_input (str): User کا input جیسا input() سے ملا۔

    Returns:
        int: Validated integer length۔

    Raises:
        ValueError: اگر input کو integer میں convert نہ کیا جا سکے (مثلاً 'abc')۔
        NegativeLengthError: اگر منفی number ہو۔
        ZeroLengthError: اگر صفر ہو۔
        MinimumLengthError: اگر minimum سے کم ہو۔
    """
    # پہلے string کو integer میں convert کرنے کی کوشش
    # اگر 'abc' یا '3.5' جیسا input ہو تو ValueError آئے گی
    try:
        length: int = int(raw_input.strip())
    except ValueError:
        raise ValueError(
            f"'{raw_input}' is not a valid integer. "
            f"only write positive number(s): Like: 12"
        )

    # Integer مل گئی، اب SecurePasswordGenerator کی validation چلاؤ
    SecurePasswordGenerator._validate_length(length)

    return length


# --- Entry Point ---

def main() -> None:
    """
    Program main entry point۔
    it takes input from user and generate secure password
    """
    print("=" * 40)
    print("   🔐 Secure Password Generator")
    print("=" * 40)

    try:
        # User سے password length لینا
        raw_input: str = input("\nEnter Password length: ")

        # Input parse اور validate کرنا
        password_length: int = parse_password_length(raw_input)

        # Generator بنانا اور password generate کرنا
        generator = SecurePasswordGenerator(length=password_length)
        password: str = generator.generate_password()

        print(f"\n Your Secure Password:\n{password}")
        print(f"\n Settings: {generator}")

    except ValueError as ve:
        # 'abc' یا '3.5' جیسے non-integer inputs
        print(f"\n Input Error: {ve}")

    except NegativeLengthError as ne:
        # '-5' جیسے منفی inputs
        print(f"\n Negative Length Error: {ne}")

    except ZeroLengthError as ze:
        # '0' input
        print(f"\n Zero Length Error: {ze}")

    except MinimumLengthError as me:
        # '3' جیسے بہت چھوٹے inputs
        print(f"\n Too Short Error: {me}")

    except Exception as e:
        # کوئی بھی unexpected error
        print(f"\n any Unexpected Error: {e}")


if __name__ == "__main__":
    main()
