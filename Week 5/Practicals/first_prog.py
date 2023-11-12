#!/usr/bin/env python3

if __name__ == '__main__':
    pass
# allows you to input a number
number = input("Enter a number: ")
# sets number as only a integer
number = int(number)
# prints out "The number entered was, " with the inputted number
print("The numbered entered was", number)
# This statment checks if the number is divisible by 10
if (number % 10) == 0:
	print("That is divisible by 10")
else:
	print("That is not divisible by 10")

