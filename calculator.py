# Define a function for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Display a menu to the user
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user input for the operation choice
choice = input("Enter choice (1/2/3/4): ")

# Check if the input is valid
if choice not in ['1', '2', '3', '4']:
    print("Invalid input")
else:
    # Get user input for the numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == '2':
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == '3':
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == '4':
        result = divide(num1, num2)
        print("Result: ", result)
