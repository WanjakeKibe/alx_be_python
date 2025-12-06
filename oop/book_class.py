# book_class.py

class Book:
    """A class representing a book with magic methods."""
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
        
        # Optional: Validate inputs
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year <= 0:
            raise ValueError("Year must be a positive integer")
    
    def __str__(self):
        """
        Return a user-friendly string representation of the book.
        
        Returns:
            str: String in format "Title by Author, published in Year"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return an official string representation that can recreate the object.
        
        Returns:
            str: String that can be used with eval() to recreate the instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed.
        """
        print(f"Deleting {self.title}")
    
    # Additional magic methods for enhanced functionality
    
    def __eq__(self, other):
        """
        Check if two books are equal (same title, author, and year).
        
        Args:
            other (Book): Another Book instance to compare with
            
        Returns:
            bool: True if books are equal, False otherwise
        """
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and 
                self.author == other.author and 
                self.year == other.year)
    
    def __lt__(self, other):
        """
        Compare books by year for sorting (less than).
        
        Args:
            other (Book): Another Book instance to compare with
            
        Returns:
            bool: True if this book was published earlier than the other
        """
        if not isinstance(other, Book):
            raise TypeError("Can only compare Book with Book")
        return self.year < other.year
    
    def __gt__(self, other):
        """
        Compare books by year for sorting (greater than).
        
        Args:
            other (Book): Another Book instance to compare with
            
        Returns:
            bool: True if this book was published later than the other
        """
        if not isinstance(other, Book):
            raise TypeError("Can only compare Book with Book")
        return self.year > other.year
    
    def __hash__(self):
        """
        Return a hash value for the book.
        Allows Book instances to be used in sets and as dictionary keys.
        
        Returns:
            int: Hash value based on title, author, and year
        """
        return hash((self.title, self.author, self.year))
    
    def __len__(self):
        """
        Return the 'length' of the book (number of characters in title).
        
        Returns:
            int: Length of the book title
        """
        return len(self.title)
    
    def __contains__(self, item):
        """
        Check if a word is in the book title (case-insensitive).
        
        Args:
            item (str): Word to search for in the title
            
        Returns:
            bool: True if word is found in title, False otherwise
        """
        if not isinstance(item, str):
            raise TypeError("Can only search for strings in book title")
        return item.lower() in self.title.lower()
