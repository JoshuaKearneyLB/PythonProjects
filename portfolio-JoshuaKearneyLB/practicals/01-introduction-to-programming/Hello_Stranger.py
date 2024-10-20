Name = input("Enter your name: ")

if Name.isspace() or Name == "":
    print("Hello, Stranger!")
else:
    print("Hello" + Name)