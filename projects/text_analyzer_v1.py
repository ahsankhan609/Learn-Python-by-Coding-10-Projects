"""
- this program helps us to understand, how to open the file and analyze it's content.
- we will see characters count of this text file with or without space
"""


def open_file(path: str) -> str:
    """
    this function will open the file and return the content of file

    Args:
        path (str): path to file
    """
    with open(path, "r") as file:
        text: str = file.read()
        return text


def analyze_text_file(text: str) -> dict[str, int]:
    print(f"Text to analyze: {text}")
    result: dict[str, int] = {
        'total_characters_including_spaces': len(text),
        'total_characters_excluding_spaces': len(text.replace(' ', '')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split()),
    }
    return result


def main() -> None:
    text: str = open_file("notes.txt")
    analysis: dict[str, int] = analyze_text_file(text)

    for key, value in analysis.items():
        print(f"{key}: {value}")


if __name__ == '__main__':
    main()

"""
Homework:
1. Create a much more user friendly message regarding the analysis (eg. "This text file contains ... ").
2. Add the top 5 most common words to the analysis message.
"""
