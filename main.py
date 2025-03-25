def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    content = get_book_text("books/frankenstein.txt")
    #print(content)
    number_of_word = get_word_count(content)
    #print(f"{number_of_word} words found in the document")
    #print(character_repeat(content))
    print(output_result(content))

#call fuction from other file
from stats import get_word_count

#character count
from stats import character_repeat

#formated output
from stats import output_result

main()