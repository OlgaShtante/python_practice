from typing import List

class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_read: int) -> float:
        percentage_read = (pages_read / self.pages) * 100
        return percentage_read

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

if __name__ == "__main__":
    book1 = Book("Игра Эндера", "Орсон Кард", 384)
    book2 = Book("Торговый баланс", "Шарон Ли, Стив Миллер", 480)

    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    for book in library.books:
        print(f"{book.title}, {book.author}, {book.pages}")

    pages_read_book1 = 100 #26%
    percentage_read_book1 = book1.read(pages_read_book1)
    print(f"'{book1.title}' - {round(percentage_read_book1,0)}%")

    pages_read_book2 = 200 #42%
    percentage_read_book2 = book2.read(pages_read_book2)
    print(f"'{book2.title}' - {round(percentage_read_book2, 0)}%")