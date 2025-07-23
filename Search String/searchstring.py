import os
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "mynotes.txt")
word_to_find=input("Enter the word to search: ")

with open(file_path,"r") as file:
    readed=file.read()
    if word_to_find in readed:
        print(f"{word_to_find} was found in {file_path}")
    else:
        print(f"{word_to_find} was not found in {file_path}")
