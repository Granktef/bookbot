
from stats import *
import sys

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
        return file_contents
    
def handle_report(count_objects, book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for count in count_objects:
        if count["letter"].isalpha():
            print(f"{count["letter"]}: {count["num"]}")
    print("============= END ===============")


def main():


    if len(sys.argv) == 2:        

        # FRANKENSTEIN_PATH = "./books/frankenstein.txt"
        book_path = sys.argv[1]

        book_content = get_book_text(book_path)

        word_count = get_word_count(book_content)    

        print(f"{word_count} words found in the document")

        char_count_dict = get_character_count(book_content)
        print(char_count_dict)
        
        counts_object = sort_counts(char_count_dict)

        handle_report(counts_object, book_path)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()

