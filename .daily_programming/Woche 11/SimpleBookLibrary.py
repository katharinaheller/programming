class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if book.isbn.lower() == isbn.lower()]

    def display_books(self):
        if not self.books:
            print("Die Bibliothek ist leer.")
        else:
            for book in self.books:
                print("Titel:", book.title)
                print("Autor:", book.author)
                print("ISBN:", book.isbn)
                print()

# Beispielverwendung
library = Library()

# Bücher hinzufügen
book1 = Book("Harry Potter und der Stein der Weisen", "J.K. Rowling", "9783551557414")
book2 = Book("Der Hobbit", "J.R.R. Tolkien", "9783423214134")
book3 = Book("Game of Thrones", "George R.R. Martin", "9780553103540")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Bücher anzeigen
library.display_books()

# Nach Autor suchen
search_author = "J.R.R. Tolkien"
print(f"Bücher von {search_author}:")
for book in library.search_by_author(search_author):
    print(book.title)

# Nach Titel suchen
search_title = "Harry Potter und der Stein der Weisen"
print(f"Buch mit dem Titel '{search_title}':")
for book in library.search_by_title(search_title):
    print(book.author)

# Nach ISBN suchen
search_isbn = "9780553103540"
print(f"Buch mit der ISBN '{search_isbn}':")
for book in library.search_by_isbn(search_isbn):
    print(book.title)
