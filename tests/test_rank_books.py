from library.book import Book
from library.library import Library, rank_books_by_popularity


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert rank_books_by_popularity(library) == []


def test_rank_books_single_book_returns_list_with_that_book():
    library = Library()
    book = Book("Clean Code", "9780132350884", "R. Martin")
    library.add_book(book)
    assert rank_books_by_popularity(library) == [book]