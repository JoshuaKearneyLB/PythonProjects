try:
    f = open('info.txt')
    print(f.readline())
except FileNotFoundError:
    print("file not found")
