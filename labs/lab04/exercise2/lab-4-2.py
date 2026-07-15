income = int(input())
if income <= 50000:
    tax = 0.0
else:
    if income > 50000:
        tax = 0.01
    else:
        tax = 0.02
totalTaxDue = tax * income
print(totalTaxDue)
