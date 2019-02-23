# Write a program that reads an integer between 0 and 1000 and adds all the digits in the integer.
# For example, if an integer is 932, the sum of all its digits is 14.
# Hint: Use the % operator to extract digits, and use the // operator to remove the extracted digit.
# For instance, 932 % 10 = 2 and 932 // 10 = 93

num = int(input("Enter number: "))
if num < 0 or num > 1000:
    print("Please enter a different number.")
else:
    sum = 0
    while num > 0:
        remainder = num % 10
        sum = sum + remainder
        num = num // 10
    print("Sum of all the digits is", sum)
