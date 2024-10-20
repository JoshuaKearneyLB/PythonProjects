password_match = False
password_valid = False
password = ""
passwordConfirm = ""
BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

while password_match != True:
    while password_valid != True:
        password = input("Enter password: ")
        if 8 <= len(password) <= 12:
            if password not in BAD_PASSWORDS:
                password_valid = True
            else:
                print("This is considered a bad password! please choose something else to stay secure.")
        else:
            print("Password must be between 8 and 12 characters! Please try again.")
    passwordConfirm = input("Confirm password: ")
    if password == passwordConfirm:
        print("Password Set")
        password_match = True
    else:
        print("Password does not match! please try again. ")