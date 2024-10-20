LoopCount = input("What number would you like to count up to? ")

for i in range(int(LoopCount)):
    counter = i+1
    if (counter % 3) and (counter % 5) == 0:
        print("Fizz Buzz")
    elif(counter % 3) == 0:
        print("Fizz")
    elif(counter % 5) == 0:
        print("Buzz")
    else:
        print(counter)