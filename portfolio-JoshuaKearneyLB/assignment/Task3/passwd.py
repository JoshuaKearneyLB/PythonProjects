# !/usr/bin/env python3

import password_modules as pm
from login import main_login
from getpass import *


if __name__ == '__main__':
    username = main_login()
    key = 5
    print("=========================")

    while True:
        # check passwords are the same after entered twice
        new_password = getpass("Enter new password: ")
        new_password_verification = getpass("Enter new password again: ")

        if new_password != new_password_verification:
            exit("Passwords do not match! exiting...")
        else:
            data = pm.get_file_content(pm.return_file_name())
            index = pm.get_user_index(username, pm.get_username_list(pm.convert_file_to_tuple_list(pm.return_file_name())))
            real_name = (pm.convert_file_to_tuple_list(pm.return_file_name())[index])[1]

            data[index] = f"{username}:{real_name}:{pm.encrypt_password(new_password, key)}\n"
            pm.write_changes_to_file(data, pm.return_file_name())
            break

    print("New password had been set.")


