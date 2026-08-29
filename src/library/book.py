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