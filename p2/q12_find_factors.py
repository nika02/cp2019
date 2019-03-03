# Write a program that reads an integer and displays all its smallest factors.
# For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.

n = int(input("Enter integer: "))
integers = []
test_int = 2

while n != 1:
    if n % test_int == 0:
        integers.append(test_int)
        n /= test_int
        test_int = 2
    else:
        test_int += 1
