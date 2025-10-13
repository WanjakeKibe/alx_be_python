class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title, author, and availability status.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute - starts as available
    
    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Mark the book as returned if it was checked out."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out
    
    def __str__(self):
        """Return a string representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize a Library with an empty collection of books."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title if it's available.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if successful, False if book not found or already checked out
        """
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                else:
                    return False  # Book was already checked out
        return False  # Book not found
    
    def return_book(self, title):
        """
        Return a book by title if it was checked out.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if successful, False if book not found or already available
        """
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return True
                else:
                    return False  # Book was already available
        return False  # Book not found
    
    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
    
    def find_book(self, title):
        """
        Find a book by title in the library.
        
        Args:
            title (str): The title to search for
            
        Returns:
            Book or None: The book if found, None otherwise
        """
        for book in self._books:
            if book.title == title:
                return book
        return None 