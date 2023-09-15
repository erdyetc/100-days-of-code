# Calculator
from calc_art import logo
# Add
def add(n1,n2):
    return n1 + n2

#Subtract
def subtract(n1,n2):
    return n1 - n2

#Multiply
def multiply(n1,n2):
    return n1 * n2

#Divide
def divide(n1,n2):
    return n1 / n2

#Define a dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))
        calculator_operation = operations[operation_symbol]
        answer = calculator_operation(num1, next_num)
        
        print(f"{num1} {operation_symbol} {next_num} = {answer}")
        
        stop_calculator = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:  ")
        if stop_calculator == "n":
            continue_calculation = False
            calculator()
        elif stop_calculator == "y":
            num1 = answer

calculator()