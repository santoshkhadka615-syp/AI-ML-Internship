"""
Week 1 - Simple File Parser
Reads a text file and reports basic stats:
- total lines
- total words
- total characters
- most common word
"""

import os


def create_sample_file(filename="sample.txt"):
    """Creates a sample text file if one doesn't exist, so the script runs out of the box."""
    if not os.path.exists(filename):
        sample_text = (
            "Python is a great language for beginners.\n"
            "Learning Python opens doors to AI and Machine Learning.\n"
            "Practice makes you better at Python every single day.\n"
        )
        with open(filename, "w") as f:
            f.write(sample_text)
        print(f"Sample file '{filename}' created.\n")


def parse_file(filename="sample.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()

    total_lines = len(lines)
    total_words = 0
    total_chars = 0
    word_freq = {}

    for line in lines:
        words = line.split()
        total_words += len(words)
        total_chars += len(line)

        for word in words:
            clean_word = word.strip(".,!?").lower()
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1

    most_common_word = max(word_freq, key=word_freq.get) if word_freq else None

    return {
        "total_lines": total_lines,
        "total_words": total_words,
        "total_characters": total_chars,
        "most_common_word": most_common_word,
        "word_frequency": word_freq,
    }


def main():
    filename = input("Enter filename to parse (press Enter to use sample.txt): ").strip()
    if not filename:
        filename = "sample.txt"
        create_sample_file(filename)

    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return

    stats = parse_file(filename)

    print("\n--- File Stats ---")
    print(f"Total Lines: {stats['total_lines']}")
    print(f"Total Words: {stats['total_words']}")
    print(f"Total Characters: {stats['total_characters']}")
    print(f"Most Common Word: {stats['most_common_word']}")


if __name__ == "__main__":
    main()