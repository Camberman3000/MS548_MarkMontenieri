# Mark Montenieri - MS548
# Week 1 project - Estimated time to complete - 4 hours
# Actual time to complete - 7 hours
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


def validate_num(num, num2):  # validate input
    while True:
        if num.isdigit() and num2.isdigit():
            return num, num2
        else:
            print("One or more of your inputs was not a number, please start over.")
            task_multiply()
            break


def task_divide():
    # perform division
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    product = int(first_num) / int(second_num)
    print((str(first_num) + " divided by " + (str(second_num) + " = " + (str(product)))))
    main()


def task_add():
    # perform addition
    first_num = input("Type first number: ")
    second_num = input("Type second number: ")
    validate_num(first_num, second_num)
    product = int(first_num) + int(second_num)
    print((str(first_num) + " plus " + (str(second_num) + " = " + (str(product)))))
    main()


def task_textblob_sentiment():
    # perform sentiment analysis using textblob
    text = input("Type a sentence to analyze, which will return the sentiment (Higher polarity = more positive & "
                 "Higher subjectivity = more opinionated): ")
    blob = TextBlob(text)
    sentiment = blob.sentiment
    print("Sentiment analysis results: " + str(sentiment))
    main()


def main():
    while True:
        print("\nWelcome to Mark's first Python Project.")
        print("Menu")
        print("1. Multiply two numbers")
        print("2. Divide two numbers")
        print("3. Add two numbers")
        print("4. Sentiment analysis")
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
                task_textblob_sentiment()
            elif choice == 5:
                print("Exiting program")
                quit()
        else:
            print("Invalid choice. Please choose a number between 1 and 5")


if __name__ == "__main__":
    main()
