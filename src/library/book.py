def borrow(self, borrower):
    """Mark this book as borrowed by the given borrower.

    Raises:
        ValueError: if the book is already borrowed or borrower name is empty.
    """
    # Validation: Check if borrower name is empty or None
    if not borrower or borrower.strip() == "":
        raise ValueError("Borrower name cannot be empty.")
    
    # Check if book is already borrowed
    if self.status == "borrowed":
        raise ValueError(f"Book '{self.title}' is already borrowed.")
    
    # Borrow the book
    self.status = "borrowed"
    self.borrower = borrower