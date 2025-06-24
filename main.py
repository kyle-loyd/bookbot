from stats import number_of_words, number_of_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])
    print(f"Found {number_of_words(content)} total words")
    unique_counts = number_of_characters(content)
    for entry in unique_counts:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()