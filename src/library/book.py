class Book:
    """Represents a single book/item in the library catalog.

    A Book may have multiple physical copies (total_copies). Borrowing a
    copy reduces available_copies; returning a copy increases it back,
    never past total_copies.
    """

    def __init__(self, title, item_id, author=None, total_copies=1):
        self.title = title
        self.item_id = item_id
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

        # Kept for backward compatibility with the original single-item
        # borrow() flow used elsewhere in the codebase.
        self.status = "available"
        self.borrower = None

    def borrow(self, borrower):
        """Mark this book as borrowed by the given borrower.

        Raises:
            ValueError: if the book is already borrowed or borrower name is empty.
        """
        # Validation: Check if borrower name is empty or None
        if not borrower or borrower.strip() == "":
            raise ValueError("Borrower name cannot be empty.")

        # Strict check: Prevent double-borrowing via attribute manipulation
        if self.status == "borrowed" or self.borrower is not None:
            raise ValueError(f"Book '{self.title}' is already borrowed.")

        # Borrow the book
        self.status = "borrowed"
        self.borrower = borrower
