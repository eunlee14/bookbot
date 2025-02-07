# main function. set default book path, set as text variable, \
# do word count, print word count and character count

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    print("--- Total Report of " + book_path + " ---")
    print(f"There are {word_count} words in this book")
    print()
    print("Character Count (Listed from most frequent)")
    for number in character_count:
        print(f"The '{number["character"]}' character was found {number["number_of_use"]} times")
    print("--- End of Report --- ")


# def opening file fn

def get_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

# def word count function

def get_word_count(text):
    word_count = len(text.split())
    return word_count

# def sort by fn to use number_of_use var for list of dictionary

def sort_by_number_of_use(dict):
    return dict["number_of_use"]


# def character count fn. listed from most frequent

def get_character_count(text):
    character_dictionary = {}
    lowered_text = text.lower()
    every_character = list(lowered_text)
    for character in every_character:
        character_dictionary[character] = \
        character_dictionary.get(character, 0) + 1
        # .get method sets default value for key even if the key is\
        # not present in dict. my_dict['key'] = my_dict.get('key', value)
    alphabets_only = []
    number_of_characters = {}
    for character in character_dictionary:
        if character.isalpha():
            number_of_characters = {
                "character": character,
                "number_of_use": character_dictionary[character]
            }
            alphabets_only.append(number_of_characters)
    alphabets_only.sort(reverse=True, key=sort_by_number_of_use)
    return alphabets_only


main()
