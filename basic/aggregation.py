class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}"for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

library = Library("Nalanda Library")

book1 = Book("Rich dad Poor dad", "Robert kiyosaki")
book2 = Book("Harry potter", "JK Rowling")
book3 = Book("Metamorphosis", "Franz kafka")

library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

print(library.name)

for book in library.list_books():
    print(book)