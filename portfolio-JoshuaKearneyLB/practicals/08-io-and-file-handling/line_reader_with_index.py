#!/usr/bin/env python3
import sys


def print_file_content(filename):
    count = 0
    bee_count = 0

    with open(filename, "r+") as f:
        for line in f:

            print(f"{count} - {line[:-1]}")
            count += 1
            if "bee" in line or ("Bee" in line):
                bee_count += 1

        print(f"The word bee is found {bee_count} times in the bee movie script")


if __name__ == '__main__':
    try:
        file = sys.argv[1]
        print_file_content(file)
    except FileNotFoundError:
        print("Could not find file, please ensure it is correct and to type the full path")
    except:
        print("No file entered")




