class Book:
    def __init__(self, name, auther, isbn):
        self.name = name
        self.auther = auther
        self.isbn = isbn

    def __str__(self):
        return f"Name: {self.name}, Auther: {self.auther}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Enter the name of the book: ")
        auther = input("Enter the name of the writer: ")
        isbn = input("Enter ISBN number: ")

        book = Book(name, auther, isbn)
        self.books.append(book)
        print("Book added successfully!!!")

    def view_book(self):
        if not self.books:
            print("No books available, sorry.")
            return

        for i, j in enumerate(self.books, start=1):
            print(f"{i}. {j}")

    def update_book(self):
        isbn = input("Enter the ISBN of the book you want to update: ")
        for i in self.books:
            if i.isbn == isbn:
                print("Currently available book at this ISBN:", i)
                i.name = input("Enter new name: ")
                i.auther = input("Enter the new author name: ")
                print("Book updated successfully")
                return

        print("Book not found")

    def delete_book(self):
        isbn = input("Enter the ISBN of the book you want to delete: ")
        for i in self.books:
            if i.isbn == isbn:
                self.books.remove(i)
                print("Book deleted successfully")
                return

        print("Book not found")

lib = Library()

while True:
    print("==== Library Menu ====")
    print("Press 1 to add")
    print("Press 2 to view books")
    print("Press 3 to update books")
    print("Press 4 to delete books")
    print("Press 5 to exit")

    choice = input("Please enter your choice: ")

    if choice == "1":
        lib.add_book()

    elif choice == "2":
        lib.view_book()

    elif choice == "3":
        lib.update_book()

    elif choice == "4":
        lib.delete_book()

    elif choice == "5":
        print("GOOD BYE!!!")
        break

    else:
        print("Please enter a valid number")
