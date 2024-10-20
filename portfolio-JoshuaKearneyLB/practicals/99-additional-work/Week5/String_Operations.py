#!\usr\bin\env python3

def contains_spaces(text_input):
    print(f"Calculating spaces in {text_input}")
    counter = 0

    while counter < len(text_input):
        if text_input[counter] == ' ':
            return True
        else:
            counter += 1
    return False

def count_characters(text_input):
    number = 0
    for char in text_input:
        number += 1
    return number

def count_spaces_in_string(text_input):
    space_count = 0
    for char in text_input:
        if char == ' ':
            space_count += 1
    return space_count

#def convert_to_upper(text_input):

#def convert_to_lower(text_input):


if __name__ == '__main__':
    user_input = input("Enter text: ")

    if contains_spaces(user_input) == True:
        print("Your input contains spaces. ")
    else:
        print("You input does not have any spaces")

    letter_count = count_characters(user_input)
    print(f"Your input: {user_input}, has {letter_count} characters")

    spaces_count = count_spaces_in_string(user_input)
    print(f"Your input: {user_input}, has {spaces_count} spaces")

