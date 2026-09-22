import pytest

from library.library import Library
from library.book import Book


@pytest.fixture
def populated_library():
    """Arrange: a Library pre-loaded with two books, multiple copies each."""
    library = Library()
    b1 = Book('Clean Code', '9780132350884', 'R. Martin', total_copies=2)
    b2 = Book('The Pragmatic Programmer', '9780135957059', 'D. Thomas', total_copies=1)
    library.add_book(b1)
    library.add_book(b2)
    return library


def test_total_available_copies_empty_catalog():
    # Arrange
    library = Library()
    # Act
    result = library.total_available_copies()
    # Assert
    assert result == 0


def test_total_available_copies_single_book():
    # Arrange
    library = Library()
    library.add_book(Book('1984', '9780451524935', 'G. Orwell', total_copies=3))
    # Act
    result = library.total_available_copies()
    # Assert
    assert result == 3


def test_total_available_copies_multiple_books(populated_library):
    # Act
    result = populated_library.total_available_copies()
    # Assert
    assert result == 3
