num_words = ""
def get_word_count(text):
    num_words = len(text.split())
    return num_words

def character_repeat(text):
    text_no_whiespace = "".join(text.lower().split())
    #list comprehension -  new_list = [expression for item in iterable]

    text_list = [ char for char in text_no_whiespace]
    count_char_repetiton = {}
    for text_char in text_list:
        if text_char in count_char_repetiton:
            count_char_repetiton[text_char] += 1
        else:
            count_char_repetiton[text_char] = 1

    return count_char_repetiton

def output_result(text):
    out_num_words = get_word_count(text)

    out_characters = character_repeat(text)
    #sort dictionary by using object view of dictionary items()
    sorted_characters = sorted(out_characters.items(), key=lambda x: x[1], reverse=True)

    dict_sorted = dict(sorted_characters)
    
    for key, value in dict_sorted.items():
        if key.isalpha() == True:
            print(f"{key}: {value}\n")
    

    return "============= END ==============="

