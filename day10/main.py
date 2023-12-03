from art import logo


def add(n1, n2):
    return n1 + n2


def sbtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': sbtract,
    '*': multiply,
    '/': divide
}


def calulator():
    num1 = float(input("What is the first number?:"))

    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operations_symbol = input("Pick an operation from the line above:")
        num2 = int(input("What is the Second number?:"))
        calculation_funcation = operations[operations_symbol]

        answer = calculation_funcation(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")
        if input(f"Tpye 'y' to connection with {answer},or type 'n' to start a new calculation") == "y":
            num1 = answer
        else:
            should_continue = False
            calulator()


calulator()

# operations_symbol = input("Pick an operation from other above:")
# num3 = int(input("What is the Second number?:"))
# calculation_funcation = operations[operations_symbol]
#
# second_answer = calculation_funcation(calculation_funcation(num1,num2),num3)
#
# print(f"{first_answer} {operations_symbol} {num3} = {second_answer}")
