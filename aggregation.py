class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_info(self) -> str:
        return f"'{self.title}' by {self.author} [ISBN: {self.isbn}]"


class Library:
    def __init__(self, name: str, books=None):
        self.name = name
        # In Aggregation, objects are created independently and passed in from the outside
        self.books = books if books is not None else []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, isbn: str) -> Book:
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return book
        return None

    def catalog(self):
        print(f"--- Library: {self.name} ---")
        for book in self.books:
            print(f" - {book.get_info()}")


if __name__ == "__main__":
    # Books exist independently of the library
    b1 = Book("The Clean Code", "Robert C. Martin", "978-0132350884")
    b2 = Book("Design Patterns", "Erich Gamma et al.", "978-0201633610")

    lib = Library("City Central Library", [b1, b2])
    lib.catalog()
