import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    match = re.search(pattern, s)

    if not match:
        raise ValueError

    hr1, min1, ampm1, hr2, min2, ampm2 = match.groups()

    # Set default minutes if not provided
    min1 = min1 if min1 else "00"
    min2 = min2 if min2 else "00"

    # Validate hours and minutes ranges
    if int(hr1) > 12 or int(hr2) > 12 or int(min1) >= 60 or int(min2) >= 60:
        raise ValueError

    return f"{to_24(hr1, min1, ampm1)} to {to_24(hr2, min2, ampm2)}"

def to_24(hr, min, ampm):
    hr = int(hr)
    if ampm == "AM":
        if hr == 12:
            hr = 0
    else: # PM
        if hr != 12:
            hr += 12
    return f"{hr:02d}:{min}"

if __name__ == "__main__":
    main()
