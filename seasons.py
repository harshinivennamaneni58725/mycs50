import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    birth_str = input("Date of Birth: ")
    try:
        birth_date = date.fromisoformat(birth_str)
    except ValueError:
        sys.exit("Invalid date")

    minutes = calculate_minutes(birth_date, date.today())
    words = minutes_to_words(minutes)
    print(words)


def calculate_minutes(birth_date, current_date):
    difference = current_date - birth_date
    return difference.days * 24 * 60


def minutes_to_words(minutes):
    # andword="" removes the word "and" while preserving native commas
    words_str = p.number_to_words(minutes, andword="")
    return f"{words_str.capitalize()} minutes"


if __name__ == "__main__":
    main()
