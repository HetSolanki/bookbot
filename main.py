from stats import get_word_count, get_character_count, sort_dir
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    sorted_list = sort_dir(character_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        key = item["key"]
        value = item["value"]
        print(f"{key}: {value}")
    print("============= END ===============")
main()
