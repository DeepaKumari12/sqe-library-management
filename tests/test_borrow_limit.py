import pytest


def _borrow_n(library, member_id, n, isbn_pool):
    """Helper: borrow n books in a row for the given member, using ISBNs
    from the shared module-scoped isbn_pool fixture instead of hardcoding
    them in every test.
    """
    for i in range(n):
        library.borrow_book(member_id, isbn_pool[i])


def test_borrow_within_limit_succeeds(empty_library, isbn_pool):
    """Representative value: member currently at 3 books, borrows a 4th."""
    _borrow_n(empty_library, "M1", 3, isbn_pool)
    new_total = empty_library.borrow_book("M1", isbn_pool[10])
    assert new_total == 4


def test_borrow_exceeding_limit_raises(empty_library, isbn_pool):
    """Representative value: member at 5 books, attempts a 6th."""
    _borrow_n(empty_library, "M1", 5, isbn_pool)
    with pytest.raises(ValueError):
        empty_library.borrow_book("M1", isbn_pool[11])


# ---------------------------------------------------------------
# Lab 6 - Boundary Value Analysis: limit is 5 books on loan
# ---------------------------------------------------------------
def test_boundary_member_at_4_books_can_borrow_one_more(empty_library, isbn_pool):
    """4 books (limit - 1): borrowing one more must succeed."""
    _borrow_n(empty_library, "M1", 4, isbn_pool)
    assert empty_library.borrow_book("M1", isbn_pool[10]) == 5


def test_boundary_member_at_5_books_is_rejected(empty_library, isbn_pool):
    """5 books (limit): borrowing one more must be rejected."""
    _borrow_n(empty_library, "M1", 5, isbn_pool)
    with pytest.raises(ValueError):
        empty_library.borrow_book("M1", isbn_pool[11])
    assert empty_library.member_loans["M1"] == 5  # count must not change


def test_boundary_member_at_6_books_is_rejected(empty_library, isbn_pool):
    """6 books (limit + 1): cannot be reached normally, so set it directly."""
    empty_library.member_loans["M1"] = 6
    with pytest.raises(ValueError):
        empty_library.borrow_book("M1", isbn_pool[11])
    assert empty_library.member_loans["M1"] == 6  # count must not change