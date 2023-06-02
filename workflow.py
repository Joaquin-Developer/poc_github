import sys


def main():
    author = sys.argv[1]
    message = sys.argv[2]
    data = sys.argv[3]
    print(author, message)
    print(type(data))
    print(data)


if __name__ == "__main__":
    main()
