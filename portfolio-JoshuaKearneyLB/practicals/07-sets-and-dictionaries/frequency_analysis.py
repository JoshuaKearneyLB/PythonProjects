
def string_to_set(s):
    s.strip()
    set_of_chars = set(s)
    return set_of_chars


def count_chars_in_string(string, set_of_chars):

    char_count = []
    for c in set_of_chars:
        char_count.append((c, string.count(c)))
    return char_count


if __name__ == "__main__":

    userinput = input("Enter the encrypted message: ")
    message = userinput.lower()

    message_tuple_list = count_chars_in_string(message, string_to_set(message))
    message_tuple_list.sort(key=lambda tup: tup[1], reverse=True)

    print(message_tuple_list[:6])
