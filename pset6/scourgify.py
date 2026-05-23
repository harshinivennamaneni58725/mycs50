import sys
import csv

def main():
    check_arguments()
    try:
        with open(sys.argv[1], "r") as infile:
            reader = csv.DictReader(infile)
            output_data = []

            for row in reader:
                # Split "Last, First" by the comma and space
                last, first = row["name"].split(", ")
                output_data.append({
                    "first": first,
                    "last": last,
                    "house": row["house"]
                })

        with open(sys.argv[2], "w", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(output_data)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
