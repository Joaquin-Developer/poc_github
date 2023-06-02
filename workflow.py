import sys


def main():
    modified_files = sys.argv[1:]

    for file in modified_files:
        print(file)
    
    print("Hi")
    print(len(modified_files))

if __name__ == "__main__":
    main()
