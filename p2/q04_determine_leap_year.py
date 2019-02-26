# Write a program that prompts the user to enter a year and determines whether it is a leap year.
# A year is a leap year if it is divisible by 4 but not 100, or is divisible by 400.


year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap")
else:
    print("Non-Leap")
