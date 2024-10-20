# A program that will convert 2 strings to an integer then multiply them and convert the result without using libraries.

numbers = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

intOfString = 0
tenCount = 1
result = 1


for k in range(2):

    stringInput = input("Enter string: ")
    i = len(stringInput)

    while i > 0:
        intOfString += ((numbers[stringInput[i-1]]) * tenCount)
        tenCount *= 10
        i -= 1

    tenCount = 1
    result *= intOfString
    intOfString = 0

print(result)