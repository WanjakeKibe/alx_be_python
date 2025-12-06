# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: If not overridden by derived class
        """
        raise NotImplementedError("Subclasses must implement area() method")
    
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: If not overridden by derived class
        """
        raise NotImplementedError("Subclasses must implement perimeter() method")
    
    def __str__(self):
        """String representation of the shape."""
        return f"{self.__class__.__name__}"
    
    def describe(self):
        """Describe the shape - demonstrates polymorphism."""
        return f"This is a {self.__class__.__name__.lower()} with area: {self.area():.2f}"


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    
    def __init__(self, length, width):
        """
        Initialize a rectangle with length and width.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive")
        
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: Area of the rectangle (length × width)
        """
        return self.length * self.width
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: Perimeter of the rectangle (2 × (length + width))
        """
        return 2 * (self.length + self.width)
    
    def is_square(self):
        """
        Check if the rectangle is a square.
        
        Returns:
            bool: True if length equals width, False otherwise
        """
        return self.length == self.width
    
    def __str__(self):
        """String representation of the rectangle."""
        shape_type = "Square" if self.is_square() else "Rectangle"
        return f"{shape_type} with length={self.length}, width={self.width}"


class Circle(Shape):
    """Derived class representing a circle."""
    
    def __init__(self, radius):
        """
        Initialize a circle with radius.
        
        Args:
            radius (float): Radius of the circle
        """
        if radius <= 0:
            raise ValueError("Radius must be positive")
        
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: Area of the circle (π × radius²)
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        
        Returns:
            float: Circumference of the circle (2 × π × radius)
        """
        return 2 * math.pi * self.radius
    
    def diameter(self):
        """
        Calculate the diameter of the circle.
        
        Returns:
            float: Diameter of the circle (2 × radius)
        """
        return 2 * self.radius
    
    def __str__(self):
        """String representation of the circle."""
        return f"Circle with radius={self.radius}"


class Triangle(Shape):
    """Additional derived class representing a triangle (bonus)."""
    
    def __init__(self, base, height, side1=None, side2=None, side3=None):
        """
        Initialize a triangle.
        
        Args:
            base (float): Base length of the triangle
            height (float): Height of the triangle
            side1, side2, side3 (float): Side lengths for perimeter calculation
        """
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive")
        
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        """
        Calculate the area of the triangle.
        
        Returns:
            float: Area of the triangle (0.5 × base × height)
        """
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        
        Returns:
            float: Perimeter if sides are provided, raises error otherwise
        """
        if self.side1 is None or self.side2 is None or self.side3 is None:
            raise ValueError("Side lengths must be provided for perimeter calculation")
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        """String representation of the triangle."""
        return f"Triangle with base={self.base}, height={self.height}"


class Square(Rectangle):
    """Derived class representing a square (inherits from Rectangle)."""
    
    def __init__(self, side):
        """
        Initialize a square with side length.
        
        Args:
            side (float): Length of each side of the square
        """
        # A square is a special case of rectangle where length = width
        super().__init__(side, side)
    
    def __str__(self):
        """String representation of the square."""
        return f"Square with side={self.length}"
