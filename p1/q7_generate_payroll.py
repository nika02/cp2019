# Write a program that reads the following information and prints a payroll statement.

Name = input("Enter name: ")
Hours = float(input("Enter number of hours worked weekly: "))
Rate = float(input("Enter hourly pay rate: "))
CPF = float(input("Enter CPF contribution rate (%): "))

Gross = Hours * Rate
Contri = Gross * CPF/100
Net = Gross - Contri

print(
    "Payroll statement for", Name,
    "Hourly pay rate: $", Rate,
    "Gross pay: $", Gross,
    "CPF Contribution at", CPF, "% = $", Contri,
    "Net pay = $", Net
    )
