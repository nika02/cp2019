# Write a recursive function reverse_int(n) that reverses the digits of an integer n:
# For example, reverse_int(12345) displays 54321.

def reverse_int(n):
    n = str(n)
    return n[::-1]

print(reverse_int(12345))
