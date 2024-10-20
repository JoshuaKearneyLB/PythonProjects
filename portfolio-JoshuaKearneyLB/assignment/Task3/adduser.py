# !/usr/bin/env python3
import password_modules as pm
import sys

if __name__ == '__main__':

    filename = pm.return_file_name()
    tuple_list = pm.convert_file_to_tuple_list(filename)

    username = pm.get_username_from_keyboard_input()
    if pm.check_username_exists(username, tuple_list):
        print("Cannot add. Most likely username already exists.")
        exit()
    else:
        key = 5
        name = pm.get_real_name_from_keyboard_input()
        password = pm.encrypt_password(pm.get_password_from_keyboard_input(), key)

        data = pm.get_file_content(filename)
        data.append(f"{username}:{name}:{password}\n")

        pm.write_changes_to_file(data, filename)
        print("User created.")
