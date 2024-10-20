def denary_to_binary(userinput):
    binary_string = " "

    while userinput != 1:
        binary_string += str(userinput % 2)
        userinput = int(userinput/2)


    return binary_string

#print(denary_to_binary(12))

number = 15
binary_string = str(bin(number)[2:])
print(list(binary_string).reverse())


