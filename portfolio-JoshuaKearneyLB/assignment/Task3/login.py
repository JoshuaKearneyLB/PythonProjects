# !/usr/bin/env python3
import password_modules as pm
from getpass import *

def main_login():

    filename = pm.return_file_name()
    tuple_list = pm.convert_file_to_tuple_list(filename)
    key = 5
    attempt_count = 3
    username = pm.get_username_from_keyboard_input()

    if pm.check_username_exists(username, pm.convert_file_to_tuple_list(filename)):

        index = pm.get_user_index(username, pm.get_username_list(tuple_list))
        encrypted_password = ((tuple_list[index])[2])
        password = pm.decrypt_password(encrypted_password, key)[:-1]

        while True:
            attempt = getpass("Enter password: ")
            if attempt_count == 0:
                exit("Too many tries, please try again later.")
            else:
                if attempt != password:
                    attempt_count -= 1
                    print(f"Incorrect password for {username}, you have {attempt_count + 1} attempts left.")
                else:
                    print(f"Access granted, welcome {(tuple_list[index])[1]}")
                    break
    else:
        exit("Username does not exist")
    return username


if __name__ == '__main__':
    main_login()