
def add_menu():
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    total = num1 + num2
    print(f"Total: {total}")
    return total

def subtract_menu():
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    total = num1 - num2
    print(f"Total: {total}")
    return total

def multiplication():
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    total = num1 * num2
    print(f"Total: {total}")
    return total
def exponents():
    num1 = float(input("Enter the base number "))
    num2 = float(input("Enter the exponent number "))
    total = num1 ** num2
    print(f"Total: {total}")
    return total

def division():
    num1 = float(input("Enter the first number "))
    num2 = float(input("Enter the second number "))
    total = num1 / num2
    print(f"Total: {total}")
    return total
def main():
    while True:
        print("""
        Welcome to the Calculator Menu!
        1 | Add
        2 | Subtract
        3 | Multiply
        4 | Exponents
        5 | Divide
        6 | Quit """)

        option = int(input("Pick an option from the options above: "))

        if option == 1:
            add_menu()

        elif option == 2:
            subtract_menu()

        elif option == 3:
            multiplication()

        elif option == 4:
            exponents()

        elif option == 5:
            division()

        elif option == 6:
            print("Quitting the program now. Goodbye!")
            break

        else:
            print("Invalid Option. Please pick 1 - 6 from the choices.")

if __name__ == "__main__":
    main()
