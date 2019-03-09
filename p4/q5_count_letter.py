# Write a recursive function count_letter(str, ch)
# that finds the number of occurrences of a specified letter ch in a string str:
# For example, count_letter("Welcome", 'e') returns 2

str = input("Enter string: ")
ch = input("Enter character: ")

def count_letter(str, ch):
    a = str.count(ch)
    print(a)

count_letter(str, ch)
