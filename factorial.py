#!/usr/bin/env python3
# Created by: someone
# Created on: November 13th, 2025
# Program calculates the factorial of a user-entered whole number
# and shows loop tracking for each iteration, with input validation.


def main():
    # prompt until a valid whole number is entered
    while True:
        try:
            number = int(input("Enter a whole number: "))
            if number < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid entry. Please enter a non-negative number.")
    print("")

    # initialize factorial and counter
    factorial = 1
    counter = 1

    # use while loop to calculate factorial
    while counter <= number:
        # show tracking message for each loop iteration
        print("Tracking {} times in loop".format(counter))
        factorial *= counter
        counter += 1

    # display the result
    print("")
    print("The factorial of {0} is {1}.".format(number, factorial))
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
