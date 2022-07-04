from art import logo


# add
def add(n1, n2):
    return n1 + n2


# substract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculater():
    print(logo)
    number1 = float(input("Enter first number: "))

    for symbol in operations:
        print(symbol)

    continued = True
    while continued:
        ops = input("Select the operation: ")
        number2 = float(input("Enter next value: "))

        functional = operations[ops]
        answer1 = round((functional(number1, number2)), 2)
        print(f"{number1} {ops} {number2} = {answer1}")

        ops2 = input(
            "Type 'y' if you would like to continue with the answer or 'n' if you wish to exit:  "
        ).lower()
        if ops2 == "y":
            number1 = answer1
        else:
            continued = False
            calculater()


calculater()
