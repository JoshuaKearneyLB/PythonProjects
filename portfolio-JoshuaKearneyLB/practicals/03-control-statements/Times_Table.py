number = int(input("Enter the times table you would like to see: "))
if number < 0:
    Number_abs = abs(number)
    for i in range(12, 0, -1):
        print(f"{Number_abs} x {i} = {Number_abs * i}")
else:
    for i in range(13):
        print(f"{number} x {i} = {number * i}")