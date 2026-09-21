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


       # ---------------------------------------------------------------
# Lab 6 - Boundary Value Analysis: limit is 5 books on loan
# ---------------------------------------------------------------
def test_boundary_member_at_4_books_can_borrow_one_more():
    """4 books (limit - 1): borrowing one more must succeed."""
    lib = Library()
    _borrow_n(lib, "M1", 4)
    assert lib.borrow_book("M1", "9780000000099") == 5


def test_boundary_member_at_5_books_is_rejected():
    """5 books (limit): borrowing one more must be rejected."""
    lib = Library()
    _borrow_n(lib, "M1", 5)
    with pytest.raises(ValueError):
        lib.borrow_book("M1", "9780000000199")
    assert lib.member_loans["M1"] == 5  # count must not change


def test_boundary_member_at_6_books_is_rejected():
    """6 books (limit + 1): cannot be reached normally, so set it directly."""
    lib = Library()
    lib.member_loans["M1"] = 6
    with pytest.raises(ValueError):
        lib.borrow_book("M1", "9780000000199")
    assert lib.member_loans["M1"] == 6  # count must not change 