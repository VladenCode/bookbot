import sys

#check if enought arguments were passed 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

#get book arguments form the command line arguments (input from terminal)
book_title = sys.argv[1]


def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    content = get_book_text(sys.argv[1])
    #print(content)
    number_of_word = get_word_count(content)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_title}...\n----------- Word Count ----------\nFound {number_of_word} total words\n--------- Character Count -------")

    #print(f"{number_of_word} words found in the document")
    #print(character_repeat(content))
    print(output_result(content))

#call fuction from other file
from stats import get_word_count

#character repeat
from stats import character_repeat

#formated output
from stats import output_result

main()