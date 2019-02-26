# Write a program that reads three edges for a triangle and determines whether the input is valid.
# The input is valid if the sum of any two edges is greater than the third edge.
# The program will compute the perimeter of the triangle if the input is valid.
# Otherwise, display that the input is invalid


s1 = int(input('Enter side 1: '))
s2 = int(input('Enter side 2: '))
s3 = int(input('Enter side 3: '))

perimeter = s1 + s2 + s3

if s1 + s2 > s3 and s1 + s3 > s2 and s2 +s3 > s1:
    print(perimeter)
else:
    print('Invalid triangle!')
