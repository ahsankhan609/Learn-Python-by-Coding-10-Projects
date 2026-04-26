import re
from collections import Counter
from typing import List, Tuple


def get_frequency(text: str, top: int | None = 5) -> List[Tuple[str, int]]:
    text = text.lower()
    words = re.findall(r'\b[a-z0-9]+\b', text)  # letters+digits only, no underscores
    counts = Counter(words)
    return counts.most_common(top) if top is not None else counts.most_common()


def main() -> None:
    try:
        user_phrase = input("enter your phrase: ").strip()
        if not user_phrase:
            raise ValueError("Please enter your phrase.")
        if all(tok.isdigit() for tok in user_phrase.split()):
            raise ValueError("Please enter a phrase containing letters.")
        freqs = get_frequency(user_phrase)
        for word, count in freqs:
            print(f"{word} - {count} times.")
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    main()
