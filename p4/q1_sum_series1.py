def sum_series1(i):
    if i == 1:
        return 1
    if i > 0:
        return sum_series1(i - 1) + 1 / i

print(sum_series1(2))
