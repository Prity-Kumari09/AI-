# Define a function that takes a list of numbers and returns the sum of these numbers
def sum_numbers(numbers):
    """
    Returns the sum of a list of numbers.

    Args:
        numbers (list): A list of numbers

    Returns:
        int: The sum of the numbers in the list
    """
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_numbers(numbers)
print("Sum of numbers using for loop:", result)

# Alternative implementation using built-in sum function
def sum_numbers_builtin(numbers):
    return sum(numbers)

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_numbers_builtin(numbers)
print("Sum of numbers using built-in sum function:", result)

# Alternative implementation using generator expression
def sum_numbers_generator(numbers):
    return sum(num for num in numbers)

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = sum_numbers_generator(numbers)
print("Sum of numbers using generator expression:", result)