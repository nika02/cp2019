# Write a program that prompts the user to enter the number of students and each student's name and score,
# and finally displays the student with the highest score and the student with the second-highest score.

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
