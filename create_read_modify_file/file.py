def create_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        print(f"{filename} created successfully\n")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("The content in file:\n" + content + "\n")
    except FileNotFoundError:
        print(f"{filename} not found")

def modify_file(filename, new_content):
    try:
        with open(filename, "a") as file:
            file.write(new_content)
            print(f"{filename} modified successfully\n")
    except FileNotFoundError:
        print(f"{filename} not found")

filename = "testing.txt"

create_file(filename, "I am just a simple content.\n")
read_file(filename)
modify_file(filename, "I am modified content.")
read_file(filename)
