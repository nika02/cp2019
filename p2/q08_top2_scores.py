# Write a program that reads an integer and displays all its smallest factors.
# For example, if the input integer is 120, the output should be as follows: 2, 2, 2, 3, 5.

num = int(input("Enter number of students: "))
class_dict = {}
count = 0
while num > count:
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    class_dict[score] = name
    count += 1

x = [ ]
for i in class_dict:
    x.append(i)
x.sort(reverse=True)
print("Student with highest score: " + class_dict.get(x[0]))
print("Student with second highest score: " + class_dict.get(x[1]))
