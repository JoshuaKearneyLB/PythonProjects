# !/usr/bin/env python3
import password_modules as pm


if __name__ == '__main__':

    filename = pm.return_file_name()
    tuple_list = pm.convert_file_to_tuple_list(filename)
    username = pm.get_username_from_keyboard_input()

    if pm.check_username_exists(username, tuple_list):
        user_index = pm.get_user_index(username, pm.get_username_list(tuple_list))
    else:
        exit("Username does not exist!")

    data = pm.get_file_content(filename)
    data[user_index] = ''
    pm.write_changes_to_file(data, filename)

