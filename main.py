import datetime
import random

print(datetime.datetime.now())
print(random.random())


def generate_headline(name: str) -> None:
    """Generate and print a headline for a software developer.

    Args:
        name (str): The name of the software developer.
    """
    print(f"{name} is a software developer.")


if __name__ == '__main__':
    name: str = "Essah"
    # print(name)
    generate_headline(name)
