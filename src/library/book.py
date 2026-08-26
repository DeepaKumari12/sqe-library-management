class Book:
    """Minimal Book class stub for the Library Management System."""

    def __init__(self, title, book_id, status="available"):
        self.title = title
        self.book_id = book_id
        self.status = status
        
           def borrow(self, borrower_name):
        """Mark this book as borrowed by the given borrower.

        Raises:
            ValueError: if the book is already borrowed.
        """
        if self.status == "borrowed":
            raise ValueError(f"Book '{self.title}' is already borrowed.")
        self.status = "borrowed"
        self.borrower = borrower_name