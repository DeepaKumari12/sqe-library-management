from library.book import Book
from library.library import Library, rank_books_by_popularity


def make_book(title, item_id, borrow_count=0):
    """Build a Book with a given borrow_count for ranking tests."""
    book = Book(title, item_id, "Test Author")
    book.borrow_count = borrow_count
    return book


def test_rank_books_empty_catalog_returns_empty_list():
    library = Library()
    assert rank_books_by_popularity(library) == []


def test_rank_books_single_book_returns_list_with_that_book():
    library = Library()
    book = make_book("Clean Code", "9780132350884")
    library.add_book(book)
    assert rank_books_by_popularity(library) == [book]


def test_rank_books_orders_by_borrow_count_descending():
    library = Library()
    low = make_book("Low Demand", "ISBN-LOW", borrow_count=1)
    high = make_book("High Demand", "ISBN-HIGH", borrow_count=5)
    library.add_book(low)
    library.add_book(high)
    assert rank_books_by_popularity(library) == [high, low]