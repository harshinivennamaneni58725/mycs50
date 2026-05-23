import sys
import csv
from tabulate import tabulate

def main():
    check_arguments()
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            table = list(reader)
            # The first row contains headers, the rest is data
            print(tabulate(table[1:], headers=table[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_arguments():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
