
file_name="mynotes.txt"
word_to_find="python"

with open(file_name,"r") as file:
    readed=file.read()
    if word_to_find in readed:
        print(f"{word_to_find} was found in {file_name}")
    else:
        print(f"{word_to_find}was not found in {file_name}")
            