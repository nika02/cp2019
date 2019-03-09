def display_pattern(n):
    a = []
    b = "1"
    a.append(b)
    for i in range(2, n+1):
        b = str(i) + " " + b
        a.append(b)

    s =[]
    for i in range(n):
        print((n-i-1) * 2 * " " + a[i])

display_pattern(20)
