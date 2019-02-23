# Write a program q1_fahrenheit_to_celsius.py that reads a Fahrenheit degree
# in double (floating point / decimal) from standard input, then converts
# it to Celsius and displays the result in standard output.
# The formula for the conversion is as follows: celsius = (5/9) * (fahrenheit - 32)

Fahrenheit = int(input("Enter Fahrenheit: "))
Celsius = (5/9) * (round(Fahrenheit, 2) - 32)
print(Celsius)
