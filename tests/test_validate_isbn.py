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

    # ---------------------------------------------------------------
# Lab 6 - Boundary Value Analysis: ISBN must be exactly 13 digits
# ---------------------------------------------------------------
@pytest.mark.parametrize('length,expected', [
    (11, False),  # limit - 2
    (12, False),  # limit - 1
    (13, True),   # limit (exactly 13 digits)
    (14, False),  # limit + 1
    (15, False),  # limit + 2
])
def test_validate_isbn_length_boundaries(length, expected):
    isbn = '9' * length
    assert validate_isbn(isbn) == expected