# Calculator
from art import logo
print(logo)

# add


def add(n1, n2):
    return n1+n2

# subtract


def subtract(n1, n2):
    return n1-n2

# multiply


def multiply(n1, n2):
    return n1*n2

# divide


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

cont = ""


def calculator():
    num1 = float(input("first number: "))
    for sign in operations:
        print(sign)
    should_cont = True

    while should_cont:
        operation_symbol = input("pick an operation: ")
        num2 = float(input("next number:  "))

        calc_function = operations[operation_symbol]
        answer = calc_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        cont = input(
            f"Type y to continue with {answer} or type new to start a new calculation or exit to leave:  ")

        if cont == "y":
            num1 = answer
        elif cont == "exit":
            should_cont = False
        elif cont == "new":
            should_cont == False
            calculator()


calculator()
