def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return a / b

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Introduce a logical error: incorrect handling of invalid input for choice
# If the choice is not in the specified range, the program will continue to execute without informing the user of the invalid choice
if choice not in ['1', '2', '3', '4']:
    print("Invalid choice")
    exit()

num1 = float(input("Enter first number: "))

# Introduce another logical error: incorrect handling of invalid input for the second number
# If the user enters a non-numeric value, the program will raise a ValueError and terminate
try:
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Introduce a bug in calculation logic: incorrect operation performed based on user's choice
# If the user selects option '4' (division), the program will perform multiplication instead
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", multiply(num1, num2))  # Intentional bug: Perform multiplication instead of division
