import sys


def main():
    author = sys.argv[1]
    message = sys.argv[2]
    modified_files = sys.argv[3]

    modified_files = sys.argv[3:]

    print(author, message)

    for file in modified_files:
        print(file)


if __name__ == "__main__":
    main()
