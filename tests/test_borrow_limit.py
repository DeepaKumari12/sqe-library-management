import pytest


@pytest.mark.parametrize(
    "starting_loans, expected_result, should_raise",
    [
        (0, 1, False),
        (2, 3, False),
        (3, 4, False),
        (4, 5, False),
        (5, None, True),
        (6, None, True),
    ],
    ids=[
        "zero_books_borrow_first",
        "two_books_borrow_third",
        "three_books_borrow_fourth",
        "at_limit_minus_one_succeeds",
        "at_limit_is_rejected",
        "above_limit_is_rejected",
    ],
)
def test_borrow_book_edge_cases(
    empty_library, isbn_pool, starting_loans, expected_result, should_raise
):
    """Consolidated borrow_book() sweep: covers the representative-value
    cases (0, 2, 3 books) and the boundary cases around the 5-book limit
    (4, 5, 6 books) that used to be 5 separate single-purpose tests.
    """
    # Arrange
    empty_library.member_loans["M1"] = starting_loans

    if should_raise:
        # Act / Assert: over the limit must raise and must not change the count
        with pytest.raises(ValueError):
            empty_library.borrow_book("M1", isbn_pool[0])
        assert empty_library.member_loans["M1"] == starting_loans
    else:
        # Act
        result = empty_library.borrow_book("M1", isbn_pool[0])
        # Assert
        assert result == expected_result
