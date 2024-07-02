#Implement a simple calculator that can perform addition, subtraction, multiplication, and division based on user input.
# Define a function for each operation
def add(x, y):
    """Add two numbers"""
    return x + y

def sub(x, y):
    """Subtract two numbers"""
    return x - y

def mul(x, y):
    """Multiply two numbers"""
    return x * y

def div(x, y):
    """Divide two numbers"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Define a main function to handle user input
def calculator():
    print("Simple Calculator")
    print("----------------")

    # Get the operation from the user
    op = input("Enter an operation (+, -, *, /): ")

    # Get the two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on the user's input
    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = sub(num1, num2)
    elif op == "*":
        result = mul(num1, num2)
    elif op == "/":
        result = div(num1, num2)
    else:
        print("Invalid operation!")
        return

    # Print the result
    print(f"{num1} {op} {num2} = {result}")

# Call the main function
calculator()
