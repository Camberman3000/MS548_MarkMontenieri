# Mark Montenieri - MS548
# Week 1 project - Estimated time to complete - 4 hours
# from textblob lib import TextBlob method
from textblob import TextBlob


def task_multiply():
    # perform multiplication
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    product = int(first_num) * int(second_num)
    print((str(first_num) + " multiplied by " + (str(second_num) + " = " + (str(product)))))
    main()


def validate_num(num, num2):#  validate input
    while True:
        if num.isdigit() and num2.isdigit():
            return
        else:
            print("One or more of your inputs was not a number, please start over.")
            task_multiply()
            break


def task_divide():
    # perform multiplication
    variable = input("Type a number: ")
    print("Your number squared is " + str(int(variable) ** 2))


def task_add():
    # perform multiplication
    variable = input("Type a number: ")
    print("Your number squared is " + str(int(variable) ** 2))


def task_subtract():
    # perform multiplication
    variable = input("Type a number: ")
    print("Your number squared is " + str(int(variable) ** 2))


def main():
    while True:
        print("\nWelcome to Mark's first Python Project.")
        print("Menu")
        print("1. Multiply two numbers")
        print("2. Divide two numbers")
        print("3. Add two numbers")
        print("4. Subtract two numbers")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            choice = int(choice)
            if choice == 1:
                task_multiply()
            elif choice == 2:
                task_divide()
            elif choice == 3:
                task_add()
            elif choice == 4:
                task_subtract()
            elif choice == 5:
                print("Exiting program")
                break
        else:
            print("Invalid choice. Please choose a number between 1 and 5")


if __name__ == "__main__":
    main()
