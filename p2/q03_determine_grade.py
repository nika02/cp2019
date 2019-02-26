# Write a program that prompts the user to enter a score between 0 and 100 inclusive


s = int(input("Enter score: "))

if s < 0 or s > 100:
    print("Invalid! Score must be within 0 - 100.")
else:
    if s <= 34:
        print("U")
    elif s >= 35 and s <= 44:
        print("S")
    elif s >= 45 and s <= 49:
        print("E")
    elif s >= 50 and s <= 54:
        print("D")
    elif s >= 55 and s <= 59:
        print("C")
    elif s >= 60 and s <= 69:
        print("B")
    else:
        print("A")
