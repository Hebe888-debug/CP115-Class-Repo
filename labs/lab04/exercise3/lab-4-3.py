hours = float(input())
if hours < 2:
    parkingFee = 0
else:
    if hours >= 3 and hours <= 5:
        parkingFee = hours - 2 * 2
    else:
        parkingFee = 6 + hours - 5 * 3
    if parkingFee > 30:
        parkingFee = 30
print(parkingFee)
