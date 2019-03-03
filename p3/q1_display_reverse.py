# Write a function reverse_int(n) to display an integer in reverse order
#For example, reverse_int(3456) displays 6543.

reverse = ''
num = input("Enter integer: ")

for i in range(len(num), 0, -1):
    reverse += num[i-1]
print(int(reverse))
