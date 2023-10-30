BOOK_FILE = "books/frankenstein.txt"

def get_words(path):
    with open(path, "r") as file:
        file_contents = file.read()
    return file_contents

def get_word_count(string_of_words):
    return len(string_of_words.split())

def get_letter_count(word_list):
    letter_counts = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
    for word in word_list:
        lower_word = word.lower()
        for letter in lower_word:
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
    return letter_counts

def print_letter_count(tuple_of_letter_counts):
    for letter, count in tuple_of_letter_counts:
        print(f"The {letter} character was found {count} times")

def sort_letter_count(dict_of_letter_counts):
    return sorted(dict_of_letter_counts.items(), key=lambda x: x[1], reverse=True) 
# print(get_letter_count(get_words(BOOK_FILE)))
result = get_letter_count(get_words(BOOK_FILE))
# print_letter_count(result)
print_letter_count(sort_letter_count(result))