def case_count(string):
    UpCount = 0
    DownCount = 0
    for i in range(len(string)):
        if string[i].isupper():
            UpCount += 1
        elif string[i].islower():
            DownCount += 1
        else:
            -1
    return UpCount, DownCount

Userstring = input("Enter a string: ")
print("Upper case count - ", case_count(Userstring)[0])
print("Lower case count - ", case_count(Userstring)[1])