


def is_line_valid(line):
    if line.count(",") == 2:
        return True
    else:
        return False

try:
    f = open('cat_shelter_1.txt', 'r+')
    total = 0
    line_count = 0

    for line in f:
        line_count += 1
        if is_line_valid(line) == False:
            print(f"Line {line_count} had an error - {line}")
    f.close()
except FileNotFoundError:
    print("File does not exist or entry is wrong")

