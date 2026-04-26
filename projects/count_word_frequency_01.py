import re
from collections import Counter


def get_frequency(text: str) -> list[tuple[str, int]]:
    """
    Description:
    this program provide list of most commonly used words in the give phrase. this function will take 1 argument:

    Parameters:
    - user_phrase - a phrase provided by user (str):

    Raises:

    Example:
        get_frequency("user phrase goes here.")

    Returns:
        - word 1 - 5
        - word 2 - 4
        - word 3 - 3
    """
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common(n=5)  # this will return the most 5 used words


def main() -> None:
    try:
        user_phrase: str = input("enter your phrase: ").strip()

        if not user_phrase:
            raise ValueError("Please enter your phrase.")
        elif user_phrase.isdigit():
            raise ValueError("Please enter a phrase, containing letters.")
        else:
            word_frequencies: list[tuple[str, int]] = get_frequency(user_phrase)

            for word, count in word_frequencies:
                print(f"{word} - {count} times.")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    main()

"""Homework:
1. Create a function that allows the user to read a file directly (such as a txt)
so the user doesn't have to copy and paste text."""
