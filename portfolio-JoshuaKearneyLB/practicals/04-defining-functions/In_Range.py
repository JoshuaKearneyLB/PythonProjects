def in_range(number):
    if number > 100 or number < 0:
        return False
    else:
        return True

cont = True
while cont == True:
    userinput = int(input("Enter a number between 0 and 100 inclusive or -1 to exit: "))
    if userinput == -1:
        cont = False
    else:
        print(in_range(userinput))