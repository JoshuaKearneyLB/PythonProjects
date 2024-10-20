#!/usr/bin/env python3

if __name__ == '__main__':

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    roman_input = input("Enter input in roman numerals, (e.g XII) : ")
    roman_list = []
    total = 0

    for char in roman_input:
        roman_list.append(char)

    for i in range(len(roman_list)):
        if i == len(roman_list) - 1:
            total += roman_dict[roman_list[i]]
            break
        if roman_dict[roman_list[i]] >= roman_dict[roman_list[i+1]]:
            total += roman_dict[roman_list[i]]
        else:
            total -= roman_dict[roman_list[i]]

    print(total)
