valid = False
while not valid:
    number = input("Enter a number: ")
    try:
        int(number)
        valid = True
    except (TypeError, ValueError):
        print("Not a number, please enter a number! ")
