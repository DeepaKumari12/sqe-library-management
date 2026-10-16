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


def test_rank_books_orders_by_borrow_count_descending():
    library = Library()
    low = Book("Low Demand", "ISBN-LOW", "Author A")
    low.borrow_count = 1
    high = Book("High Demand", "ISBN-HIGH", "Author B")
    high.borrow_count = 5
    library.add_book(low)
    library.add_book(high)
    assert rank_books_by_popularity(library) == [high, low]