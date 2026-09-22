class LibraryIOError(Exception):
    """Raised when the library catalog cannot be written to disk."""
    pass


def fine_tier(days_overdue):
    """Map days overdue to a fine tier label."""
    if not isinstance(days_overdue, int):
        raise TypeError("days_overdue must be a whole number of days.")
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
    """Tracks member loans and the book catalog."""

    MAX_BOOKS_PER_MEMBER = 5

    def __init__(self):
        self.member_loans = {}
        self.catalog = {}  # item_id/isbn -> Book

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

    def add_book(self, book):
        """Add a Book to the catalog, keyed by its item_id/isbn."""
        self.catalog[book.item_id] = book

    def total_available_copies(self):
        """Sum of available_copies across every book in the catalog."""
        return sum(book.available_copies for book in self.catalog.values())

    def export_catalog(self, path):
        """Write the book catalog to disk, one line per book.

        Raises:
            LibraryIOError: if the file cannot be written (wraps the
            original OSError so callers never see the raw OSError).
        """
        try:
            with open(path, "w") as f:
                for book in self.catalog.values():
                    line = "{},{},{}/{}\n".format(
                        book.title, book.item_id,
                        book.available_copies, book.total_copies,
                    )
                    f.write(line)
        except OSError as e:
            raise LibraryIOError(
                "Failed to export catalog to '" + path + "': " + str(e)
            ) from e


def validate_isbn(isbn):
    """Validate that isbn is exactly 13 numeric digits."""
    return isinstance(isbn, str) and len(isbn) == 13 and isbn.isdigit()
