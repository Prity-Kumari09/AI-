#A program that shows, implementation of error handling in Python
# Example program that demonstrates error handling in Python

def divide_numbers(a, b):
    """
    Divide two numbers and return the result
    """
    try:
        # Attempt to divide the numbers
        result = a / b
        return result
    except ZeroDivisionError:
        # Handle the error if b is zero
        print("Error: Cannot divide by zero!")
        return None
    except TypeError:
        # Handle the error if a or b is not a number
        print("Error: Invalid input type. Please enter numbers only.")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Error: An unexpected error occurred - {e}")
        return None

# Test the function with valid inputs
print(divide_numbers(10, 2))  # Output: 5.0

# Test the function with invalid inputs
print(divide_numbers(10, 0))  # Output: Error: Cannot divide by zero!
print(divide_numbers("10", 2))  # Output: Error: Invalid input type. Please enter numbers only.
print(divide_numbers(10, "2"))  # Output: Error: Invalid input type. Please enter numbers only.