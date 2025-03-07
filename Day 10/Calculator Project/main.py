from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    while True:
        first_number = int(input("What is the first number: "))

        while True:
            print("+\n-\n*\n/")
            math_operator = input("Pick an operation: ")
            second_number = int(input("What's the next number?: "))

            result = calc_dict[math_operator](first_number, second_number)
            print(f"{first_number} {math_operator} {second_number} = {result}")

            ask_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation (or 'q' to quit): ").lower()

            if ask_continue == "y":
                first_number = result
            elif ask_continue == "n":
                break  #
            elif ask_continue == "q":
                print("*********************Exit Program*******************************")
                return

calculator()
