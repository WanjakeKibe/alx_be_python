# class_static_methods_demo.py

class Calculator:
    """A class demonstrating class methods and static methods."""
    
    # Class attributes
    calculation_type = "Arithmetic Operations"
    version = "1.0"
    total_calculations = 0  # Track total calculations performed
    
    def __init__(self, name="Default Calculator"):
        """Instance initialization."""
        self.name = name
        self.instance_calculations = 0
        Calculator.total_calculations += 1
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to class or instance state.
        They're like regular functions but belong to the class namespace.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
        """
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Static method to subtract b from a."""
        return a - b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to class state via 'cls' parameter.
        They can modify class attributes.
        
        Args:
            cls: Reference to the class (Calculator)
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        cls.total_calculations += 1  # Modify class attribute
        return a * b
    
    @classmethod
    def divide(cls, a, b):
        """Class method to divide a by b with error handling."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        print(f"Calculation type: {cls.calculation_type}")
        cls.total_calculations += 1
        return a / b
    
    @classmethod
    def get_calculation_stats(cls):
        """Class method to get calculation statistics."""
        return {
            "calculation_type": cls.calculation_type,
            "version": cls.version,
            "total_calculations": cls.total_calculations
        }
    
    @classmethod
    def create_scientific_calculator(cls):
        """Factory method: Alternative constructor."""
        scientific_calc = cls(name="Scientific Calculator")
        scientific_calc.calculation_type = "Scientific Operations"
        return scientific_calc
    
    @classmethod
    def set_calculation_type(cls, new_type):
        """Class method to modify class attribute."""
        cls.calculation_type = new_type
        print(f"Calculation type changed to: {new_type}")
    
    # Regular instance method
    def calculate_power(self, base, exponent):
        """Instance method to calculate power."""
        self.instance_calculations += 1
        Calculator.total_calculations += 1
        return base ** exponent
    
    def get_instance_stats(self):
        """Get instance-specific statistics."""
        return {
            "name": self.name,
            "instance_calculations": self.instance_calculations,
            "total_class_calculations": Calculator.total_calculations
        }


class AdvancedCalculator(Calculator):
    """Inherited class to demonstrate class method inheritance."""
    
    calculation_type = "Advanced Arithmetic Operations"
    
    @classmethod
    def power(cls, a, b):
        """Class method to calculate power."""
        print(f"Calculation type: {cls.calculation_type}")
        cls.total_calculations += 1
        return a ** b
    
    @staticmethod
    def sqrt(a):
        """Static method to calculate square root."""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5
    
    @classmethod
    def get_all_operations(cls):
        """Demonstrate accessing parent class attributes."""
        return {
            "parent_type": super().calculation_type,
            "child_type": cls.calculation_type,
            "version": cls.version
        }


class GeometryCalculator:
    """Another class to demonstrate different use cases."""
    
    PI = 3.141592653589793
    
    @staticmethod
    def circle_area(radius):
        """Static method: Doesn't need class state."""
        return GeometryCalculator.PI * (radius ** 2)
    
    @staticmethod
    def rectangle_area(length, width):
        """Static method."""
        return length * width
    
    @classmethod
    def get_pi_value(cls):
        """Class method: Can access class attributes."""
        return cls.PI
    
    @classmethod
    def set_pi_precision(cls, precision):
        """Class method: Can modify class state."""
        import math
        cls.PI = round(math.pi, precision)
        return cls.PI


class UnitConverter:
    """Demonstrating class methods as factory methods."""
    
    def __init__(self, unit_type):
        self.unit_type = unit_type
    
    @classmethod
    def create_temperature_converter(cls):
        """Factory method: Creates specific converter."""
        return cls(unit_type="Temperature")
    
    @classmethod
    def create_length_converter(cls):
        """Factory method: Creates specific converter."""
        return cls(unit_type="Length")
    
    @classmethod
    def create_weight_converter(cls):
        """Factory method: Creates specific converter."""
        return cls(unit_type="Weight")
    
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Static method: Unit conversion."""
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Static method: Unit conversion."""
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def meters_to_feet(meters):
        """Static method: Unit conversion."""
        return meters * 3.28084
    
    @staticmethod
    def feet_to_meters(feet):
        """Static method: Unit conversion."""
        return feet / 3.28084
