# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with comprehensive error handling.
    
    Args:
        numerator (str): The numerator as a string
        denominator (str): The denominator as a string
    
    Returns:
        str: Result of division or error message
    """
    try:
        # Try to convert inputs to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform division
        result = num / den
        
        # Format result to remove unnecessary decimal places for whole numbers
        if result.is_integer():
            return f"The result of the division is {int(result)}"
        else:
            return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except Exception as e:
        # Catch any other unexpected errors
        return f"Unexpected error: {str(e)}"
