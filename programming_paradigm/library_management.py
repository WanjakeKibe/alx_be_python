# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute (indicated by single underscore)
    
    def check_out(self):
        """
        Check out the book if it's available.
        
        Returns:
            bool: True if book was checked out successfully, False if already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """
        Return the book to the library.
        
        Returns:
            bool: True if book was returned successfully, False if already available
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if available, False if checked out
        """
        return not self._is_checked_out
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Book info in format "Title by Author"
        """
        return f"{self.title} by {self.author}"


class Library:
    """A class representing a library that manages books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []  # Private list to store Book instances
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): The Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def find_book(self, title):
        """
        Find a book by title (case-insensitive).
        
        Args:
            title (str): The title of the book to find
            
        Returns:
            Book or None: The book if found, None otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def check_out_book(self, title):
        """
        Check out a book from the library by title.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was checked out successfully, False otherwise
        """
        book = self.find_book(title)
        if book and book.check_out():
            return True
        return False
    
    def return_book(self, title):
        """
        Return a book to the library by title.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was returned successfully, False otherwise
        """
        book = self.find_book(title)
        if book and book.return_book():
            return True
        return False
    
    def list_available_books(self):
        """
        List all available books in the library.
        
        Returns:
            list: List of available Book instances
        """
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
        
        return available_books
    
    def get_all_books(self):
        """
        Get all books in the library (both available and checked out).
        
        Returns:
            list: List of all Book instances
        """
        return self._books
    
    def count_books(self):
        """
        Count all books in the library.
        
        Returns:
            int: Total number of books
        """
        return len(self._books)
    
    def count_available_books(self):
        """
        Count available books in the library.
        
        Returns:
            int: Number of available books
        """
        return len(self.list_available_books())
