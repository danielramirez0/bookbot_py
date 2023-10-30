path = "books/frankenstein.txt"
with open(path, "r") as file:
    file_contents = file.read()
    word_count = len(file_contents.split())
    print("The number of words in the file is:", word_count)