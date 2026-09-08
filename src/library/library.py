def fine_tier(days_overdue):
    """Map days overdue to a fine tier label."""
    if days_overdue < 0:
        raise ValueError("days_overdue cannot be negative.")
    if days_overdue == 0:
        return "None"
    if 1 <= days_overdue <= 7:
        return "Low"
    if 8 <= days_overdue <= 14:
        return "Medium"
    if 15 <= days_overdue <= 30:
        return "High"
    return "Severe"


class Library:
    """Tracks how many books each member currently has on loan."""

    MAX_BOOKS_PER_MEMBER = 5

    def __init__(self):
        self.member_loans = {}

    def borrow_book(self, member_id, isbn):
        """Register a new loan for member_id."""
        current = self.member_loans.get(member_id, 0)
        if current >= self.MAX_BOOKS_PER_MEMBER:
            raise ValueError(
                "Member '" + member_id + "' already has the maximum of "
                + str(self.MAX_BOOKS_PER_MEMBER) + " books on loan."
            )
        self.member_loans[member_id] = current + 1
        return self.member_loans[member_id]


def validate_isbn(isbn):
    """Validate that isbn is exactly 13 numeric digits."""
    return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()