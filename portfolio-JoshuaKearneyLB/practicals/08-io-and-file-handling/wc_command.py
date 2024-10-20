import sys

if __name__ == "__main__":
    file = sys.argv[1]

    with open(file, "r") as f:
        content = f.readlines()
        print(content)