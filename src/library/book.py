class Book:
    """Minimal Book class stub for the Library Management System."""

    def __init__(self, title, book_id, status="available"):
        self.title = title
        self.book_id = book_id
        self.status = status
        
    def borrow(self, borrower_name):
        self.status = "borrowed"
        self.borrower = borrower_name