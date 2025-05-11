# task1-package-management/date_calculator.py

from datetime import datetime

def calculate_date_difference(date1_str, date2_str, date_format="%Y-%m-%d"):
    """
    Calculate the difference in days between two dates.

    Args:
        date1_str (str): The first date string.
        date2_str (str): The second date string.
        date_format (str): The format in which the dates are provided. Default is "%Y-%m-%d".

    Returns:
        int: The number of days between the two dates.

    Raises:
        ValueError: If the date strings do not match the expected format.

    Example:
        >>> calculate_date_difference("2025-01-01", "2025-01-10")
        9
        >>> calculate_date_difference("2025-01-10", "2025-01-01")
        9
        >>> calculate_date_difference("01-01-2025", "10-01-2025", "%d-%m-%Y")
        9
    """
     # Parse the input strings into datetime objects
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        #calculate difference in days
        difference = abs((date2 - date1).days)
        return difference
    except ValueError as ve:
        raise ValueError(f"Invalid date format or values: {ve}")

# Optional: Run a test if this script is executed directly
if __name__ == "__main__":
    try:
        d1 = input("Enter the first date (YYYY-MM-DD): ")
        d2 = input("Enter the second date (YYYY-MM-DD): ")
        result = calculate_date_difference(d1, d2)
        print(f"The difference is {result} days.")
    except ValueError as error:
        print(f"Error: {error}")
