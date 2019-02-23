# Write a program that reads a number in miles, converts it to kilometres, and displays the result.
# One mile is 1.60934 kilometres. Display your answer correct to 3 decimal places.

Miles = int(input("Enter distance in miles: "))
Kilometres = Miles * 1.60934
print(round(Kilometres, 3))
