import pytest

from library.library import validate_isbn


@pytest.mark.parametrize('isbn,expected', [
    ('9780306406157', True),   # valid 13-digit ISBN
    ('', False),               # empty string
    ('978030640615', False),   # too-short (12 digits)
    ('97803064061X5', False),  # contains a letter
])
def test_validate_isbn_classes(isbn, expected):
    assert validate_isbn(isbn) == expected