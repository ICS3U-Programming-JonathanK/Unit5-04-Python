#!/usr/bin/env python3

# Created by: Jonathan Kene
# Created on: June 4, 2021
# This program asks the user for an operator and two numbers to display the
# result of the two numbers and the operator they wihs to use for the numbers

def calculate(operator, first_num, sec_num):
    result = float(-1)
    if operator == "+":
        result = first_num + sec_num
    elif operator == "-":
        result = first_num - sec_num
    elif operator == "*":
        result = first_num * sec_num
    elif operator == "/":
        result = first_num / sec_num
    elif operator == "%":
        result = first_num % sec_num
    else:
        result = float(-1)
    return result


def main():
    print("This program will perform calculations between two given numbers")

    # asks the user for an operator to use on the two numbers
    operation = input("Please type in the math operation you"
                      " would like to complete (+, -, *, /, %): ")

    if (operation == "+"):
        while True:
            # this function gets the two numbers from the user
            user_first_num_string = input("Enter first number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_first_num_float = float(user_first_num_string)
                if (user_first_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_first_num_float))
                else:
                    break
            except ValueError:
                print("Please enter a valid number")
                break
        while True:
            user_sec_num_string = input("Enter second number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_sec_num_float = float(user_sec_num_string)
                if (user_sec_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_sec_num_float))
                else:
                    break
            except ValueError:
                print("{} is not a valid number". format(user_sec_num_string))
        results = calculate(operation, user_first_num_float,
                            user_sec_num_float)
        print("{} + {} equals {}". format(user_first_num_float,
                                          user_sec_num_float, results))
    elif (operation == "-"):
        while True:
            # this function gets the two numbers from the user
            user_first_num_string = input("Enter first number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_first_num_float = float(user_first_num_string)
                print("")
                if (user_first_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_first_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not a"
                      "valid number". format(user_first_num_string))

        while True:
            user_sec_num_string = input("Enter second number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_sec_num_float = float(user_sec_num_string)
                print("")
                if (user_sec_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_sec_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not a valid number". format(user_sec_num_string))

        results = calculate(operation, user_first_num_float,
                            user_sec_num_float)
        print("{} - {} equals {}". format(user_first_num_float,
                                          user_sec_num_float, results))
    elif (operation == "*"):
        while True:
            # this function gets the two numbers from the user
            user_first_num_string = input("Enter first number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_first_num_float = float(user_first_num_string)
                print("")
                if (user_first_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_first_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not"
                      " a valid number". format(user_first_num_string))

        while True:
            user_sec_num_string = input("Enter second number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_sec_num_float = float(user_sec_num_string)
                print("")
                if (user_sec_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_sec_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not a valid number". format(user_sec_num_string))

        results = calculate(operation, user_first_num_float,
                            user_sec_num_float)
        print("{} x {} equals {}". format(user_first_num_float,
                                          user_sec_num_float, results))
    elif (operation == "/"):
        while True:
            # this function gets the two numbers from the user
            user_first_num_string = input("Enter first number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_first_num_float = float(user_first_num_string)
                print("")
                if (user_first_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_first_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not"
                      " a valid number". format(user_first_num_string))

        while True:
            user_sec_num_string = input("Enter second number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_sec_num_float = float(user_sec_num_string)
                print("")
                if (user_sec_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_sec_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not a valid number". format(user_sec_num_string))

        results = calculate(operation, user_first_num_float,
                            user_sec_num_float)
        print("{} ÷ {} equals {}". format(user_first_num_float,
                                          user_sec_num_float, results))
    elif (operation == "%"):
        while True:
            # this function gets the two numbers from the user
            user_first_num_string = input("Enter first number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_first_num_float = float(user_first_num_string)
                print("")
                if (user_first_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_first_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not"
                      " a valid number". format(user_first_num_string))

        while True:
            user_sec_num_string = input("Enter second number: ")

        # make sure if the user types anything but an integer, it's not valid
            try:
                user_sec_num_float = float(user_sec_num_string)
                print("")
                if (user_sec_num_float <= 0):
                    print("{} is not a "
                          "positive number". format(user_sec_num_float))
                else:
                    print("")
                    break
            except ValueError:
                print("{} is not a valid number". format(user_sec_num_string))

        results = calculate(operation, user_first_num_float,
                            user_sec_num_float)
        print("{} % {} gives the remainder {}". format(user_first_num_float,
                                                       user_sec_num_float,
                                                       results))
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
