#------------------ Simple Calculator ------------------

# plus
def add(a, b):
    return a + b

# minus function
def subtract(a, b):
    return a - b

# multiply function
def multiply(a, b):
    return a * b

# divide function
def divide(a, b):
    if b == 0:
        raise ValueError("Error! Division by zero is not allowed.")
    return a / b

# modulus function
def modulus(a, b):
    if b == 0:
        raise ValueError("Error! Division by zero is not allowed.")
    return a % b


# -------printing the results of operations-------
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")

    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice == '6':
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")

        else:
            print("Invalid input! Please select from 1 to 5.")

    except ValueError:
        print("Error! Please enter valid numbers.")
