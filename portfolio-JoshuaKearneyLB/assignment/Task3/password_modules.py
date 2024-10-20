# !/usr/bin/ env python3
import sys
from getpass import *


def return_file_name():
    try:
        filename = str(sys.argv[1])
        return filename
    except FileNotFoundError:
        exit("No file argument passed.")


def convert_file_to_tuple_list(filename):
    tuple_list = []

    with open(filename, 'r') as f:
        for line in f:
            tuple_list.append(line.split(':'))
    return tuple_list


# get list of usernames
def get_username_list(tuple_list):
    usernames = []
    for item in tuple_list:
        usernames.append(item[0])
    return usernames


# encrypt password
def encrypt_password(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        unicode = ord(char)
        unicode += key
        cipher_text += (chr(unicode))
    return str(cipher_text)


# decrypt password
def decrypt_password(cipher_text, key):
    plaintext = ""
    for char in cipher_text:
        unicode = ord(char)
        unicode -= key
        plaintext += (chr(unicode))
    return str(plaintext)


# get password
def get_password_from_keyboard_input():
    password = getpass("Enter your password: ")
    return password


# check if username exists, Returns a BOOL based on if username exists or not
def check_username_exists(username, tuple_list):
    username_list = get_username_list(tuple_list)

    if username in username_list:
        return True
    else:
        return False


# get the username
def get_username_from_keyboard_input():
    username = input("Enter username: ")
    return username


def get_real_name_from_keyboard_input():
    real_name = input("Enter your real name: ")
    return real_name


# get the user index by username
def get_user_index(username, username_list):
    return username_list.index(username)


# upload file changes made by user
def write_changes_to_file(data, filename):

    file = open(filename, 'w')
    file.writelines(data)


# get the file content in a list of strings
def get_file_content(filename):

    file = open(filename, 'r')
    data = file.readlines()

    return data

