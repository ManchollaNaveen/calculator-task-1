# first write functions  of a simple calculator (*, /, +, -)
def add(x, y):
    return x + y
def subtarct(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero." 
    return x / y

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(f"{number1} + {number2} = {add(number1, number2)}")
elif operation == '-':
    print(f"{number1} - {number2} = {subtarct(number1, number2)}")
elif operation == '*':
    print(f"{number1} * {number2} = {multiply(number1, number2)}")
elif operation == '/':
    print(f"{number1} / {number2} = {divide(number1, number2)}")
else:
    print("Invalid operation!")


if __name__ == "__main__":
    pass
