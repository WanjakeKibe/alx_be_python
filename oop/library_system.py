# library_system.py

class Book:
    """Base class representing a book."""
    
    def __init__(self, title, author):
        """
        Initialize a Book with title and author.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def get_info(self):
        """
        Get information about the book.
        
        Returns:
            str: Book information in a standard format
        """
        return f"Book: {self.title} by {self.author}"
    
    def __str__(self):
        """String representation of the book."""
        return self.get_info()
    
    def __repr__(self):
        """Official string representation."""
        return f"Book('{self.title}', '{self.author}')"


class EBook(Book):
    """Derived class representing an electronic book."""
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): File size in kilobytes (KB)
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.file_size = file_size
        
        # Validate file_size
        if not isinstance(file_size, int):
            raise TypeError("File size must be an integer")
        if file_size <= 0:
            raise ValueError("File size must be positive")
    
    def get_info(self):
        """
        Get information about the ebook.
        
        Returns:
            str: EBook information with file size
        """
        base_info = super().get_info().replace("Book:", "EBook:")
        return f"{base_info}, File Size: {self.file_size}KB"
    
    def get_file_size_mb(self):
        """
        Get file size in megabytes.
        
        Returns:
            float: File size in MB
        """
        return self.file_size / 1024
    
    def __repr__(self):
        """Official string representation."""
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"


class PrintBook(Book):
    """Derived class representing a physical printed book."""
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): Number of pages in the book
        """
        # Call the parent class constructor
        super().__init__(title, author)
        self.page_count = page_count
        
        # Validate page_count
        if not isinstance(page_count, int):
            raise TypeError("Page count must be an integer")
        if page_count <= 0:
            raise ValueError("Page count must be positive")
    
    def get_info(self):
        """
        Get information about the print book.
        
        Returns:
            str: PrintBook information with page count
        """
        base_info = super().get_info().replace("Book:", "PrintBook:")
        return f"{base_info}, Page Count: {self.page_count}"
    
    def estimate_read_time(self, pages_per_hour=30):
        """
        Estimate reading time for the book.
        
        Args:
            pages_per_hour (int): Average pages read per hour (default: 30)
            
        Returns:
            float: Estimated reading time in hours
        """
        return self.page_count / pages_per_hour
    
    def __repr__(self):
        """Official string representation."""
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"


class Library:
    """Class representing a library that manages books (composition)."""
    
    def __init__(self):
        """Initialize an empty library."""
        self.books = []  # Composition: Library contains Book objects
    
    def add_book(self, book):
        """
        Add a book to the library.
        
        Args:
            book (Book): A Book, EBook, or PrintBook instance
            
        Raises:
            TypeError: If the object is not a Book instance
        """
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to the library")
        self.books.append(book)
        print(f"Added to library: {book.title}")
    
    def list_books(self):
        """List all books in the library with their details."""
        if not self.books:
            print("The library is empty.")
            return
        
        print("\n" + "=" * 60)
        print("LIBRARY CATALOG")
        print("=" * 60)
        
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book.get_info()}")
        
        print("=" * 60)
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: Number of books
        """
        return len(self.books)
    
    def get_books_by_type(self):
        """
        Get counts of books by type.
        
        Returns:
            dict: Dictionary with book type counts
        """
        counts = {
            'Book': 0,
            'EBook': 0,
            'PrintBook': 0
        }
        
        for book in self.books:
            if isinstance(book, EBook):
                counts['EBook'] += 1
            elif isinstance(book, PrintBook):
                counts['PrintBook'] += 1
            else:
                counts['Book'] += 1
        
        return counts
    
    def search_books(self, keyword):
        """
        Search books by title or author.
        
        Args:
            keyword (str): Search term
            
        Returns:
            list: List of matching Book objects
        """
        keyword = keyword.lower()
        results = []
        
        for book in self.books:
            if (keyword in book.title.lower() or 
                keyword in book.author.lower()):
                results.append(book)
        
        return results
    
    def remove_book(self, title):
        """
        Remove a book from the library by title.
        
        Args:
            title (str): Title of the book to remove
            
        Returns:
            bool: True if book was removed, False if not found
        """
        for i, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                removed_book = self.books.pop(i)
                print(f"Removed from library: {removed_book.title}")
                return True
        return False
