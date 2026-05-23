import sys

def main():
    check_arguments()
    try:
        with open(sys.argv[1], "r") as file:
            count = 0
            for line in file:
                if is_code_line(line):
                    count += 1
            print(count)
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def is_code_line(line):
    # Strip whitespace to check for blank lines or comments
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("#"):
        return False
    return True

if __name__ == "__main__":
    main()
