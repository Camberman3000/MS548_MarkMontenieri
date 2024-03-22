# Mark Montenieri - MS548
# Week 1 project - Estimated time to complete - 4 hours
# Actual time to complete - 7 hours
# from textblob lib import TextBlob method
from textblob import TextBlob


class TuplesParent:
    def __init__(self):
        return


class TuplesChild(TuplesParent):  # Child class
    def task_child_tuple(self, tuple_data):
        x = ("Tuple child 1", "Tuple child 2", "Tuple child 3")
        print("Tuple Child results: " + str(tuple_data))

        print("Child Tuple: " + str(tuple_data))
        outfile = open("output.txt", "a")  # Open file
        outfile.write("Menu option 5 (Tuple) output: ")  # Write to file
        outfile.write(str(tuple_data) + "\n")  # Write product to file
        outfile.close()  # Close the file


def task_multiply():
    # perform multiplication
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    product_result = int(first_num) * int(second_num)
    print((str(first_num) + " multiplied by " + (str(second_num) + " = " + (str(product_result)))))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 1 (Multiply) output: ")  # Write to file
    outfile.write(str(product_result) + "\n")  # Write product to file
    outfile.close()  # Close the file
    menu_loop()


def task_divide():
    # perform division
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    quotient_result = int(first_num) / int(second_num)
    print((str(first_num) + " divided by " + (str(second_num) + " = " + (str(quotient_result)))))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 2 (Division) output: ")  # Write to file
    outfile.write(str(quotient_result) + "\n")  # Write product to file
    outfile.close()  # Close the file
    menu_loop()


def task_add():
    # perform addition
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    sum_result = int(first_num) + int(second_num)
    print((str(first_num) + " plus " + (str(second_num) + " = " + (str(sum_result)))))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 3 (Addition) output: ")  # Write to file
    outfile.write(str(sum_result) + "\n")  # Write product to file
    outfile.close()  # Close the file
    menu_loop()


def validate_num(num, num2):  # validate input
    while True:
        if num.isdigit() and num2.isdigit():
            return num, num2
        else:
            print("One or more of your inputs was not a number, please start over.")
            task_multiply()
            break


def task_textblob_sentiment():
    # perform sentiment analysis using textblob
    text = input("Type a sentence to analyze, which will return the sentiment (Higher polarity = more positive & "
                 "Higher subjectivity = more opinionated): ")
    blob = TextBlob(text)
    sentiment_result = blob.sentiment
    print("Sentiment analysis results: " + str(sentiment_result))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 4 (Sentiment) output: ")  # Write to file
    outfile.write(str(sentiment_result) + "\n")  # Write product to file
    outfile.close()  # Close the file
    menu_loop()


def task_tuple():
    simple_tuple = ("Tuple item 1", "Tuple item 2", "Tuple item 3", "Tuple item 4")

    print("Tuple results: " + str(simple_tuple))
    outfile = open("output.txt", "a")  # Open file
    outfile.write("Menu option 5 (Tuple) output: ")  # Write to file
    outfile.write(str(simple_tuple) + "\n")  # Write product to file
    outfile.close()  # Close the file

    child_tuple = ("Tuple child 1", "Tuple child 2", "Tuple child 3", "Tuple child 4")
    x = TuplesChild()
    x.task_child_tuple(child_tuple)

    menu_loop()


def menu_loop():
    try:
        print("\nWelcome to Mark's first Python Project.")
        print("Menu")
        print("1. Multiply two numbers")
        print("2. Divide two numbers")
        print("3. Add two numbers")
        print("4. Sentiment analysis")
        print("5. Print Tuple")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        if choice.isdigit() and 1 <= int(choice) <= 6:
            choice = int(choice)
            if choice == 1:
                task_multiply()
            elif choice == 2:
                task_divide()
            elif choice == 3:
                print("CHOICE ADD")
                task_add()
            elif choice == 4:
                task_textblob_sentiment()
            elif choice == 5:
                task_tuple()
            elif choice == 6:
                print("Exiting program")
                quit()
        else:
            print("Invalid choice. Please choose a number between 1 and 5")
    except TypeError:
        print("Try Exception")


if __name__ == "__main__":
    menu_loop()
