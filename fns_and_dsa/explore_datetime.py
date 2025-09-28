from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in YYYY-MM-DD HH:MM:SS format
    """
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    return current_date

def calculate_future_date(days):
    """
    Calculate and return the future date after adding specified days
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    return future_date

def main():
    # Part 1: Display Current Date and Time
    current_date = display_current_datetime()
    
    # Part 2: Calculate Future Date
    try:
        days_input = input("Enter the number of days to add to the current date: ")
        days = int(days_input)
        
        future_date = calculate_future_date(days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("Error: Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()