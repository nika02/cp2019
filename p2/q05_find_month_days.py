# Write a program that prompts the user to enter the month and year, and displays the number of days in the month.
# For example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days.
# If the user entered month 3 and year 2005, the program should display that March 2005 has 31 days.


from calendar import monthrange

month = int(input("Enter month: "))
year = int(input("Enter year: "))

print(monthrange(year, month)[1])
