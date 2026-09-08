import pytest

from library.library import Library


def _borrow_n(library, member_id, n):
    """Helper: borrow n books in a row for the given member."""
    for i in range(n):
        library.borrow_book(member_id, f"97800000000{i:02d}")


def test_borrow_within_limit_succeeds():
    """Representative value: member currently at 3 books, borrows a 4th."""
    lib = Library()
    _borrow_n(lib, "M1", 3)
    new_total = lib.borrow_book("M1", "9780000000099")
    assert new_total == 4


def test_borrow_exceeding_limit_raises():
    """Representative value: member at 5 books, attempts a 6th."""
    lib = Library()
    _borrow_n(lib, "M1", 5)
    with pytest.raises(ValueError):
        lib.borrow_book("M1", "9780000000199")