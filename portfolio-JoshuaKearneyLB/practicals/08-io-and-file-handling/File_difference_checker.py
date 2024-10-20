import sys


def get_file_hash(filename):

    with open(filename, "r") as f:
        content = f.readlines()

    hash_of_contents = hash(str(content))
    return hash_of_contents


if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if get_file_hash(file1) == get_file_hash(file2):
        print("Files are the same!")
    else:
        print("There is a difference between the two files")
