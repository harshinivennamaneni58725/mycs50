def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length requirements
    if not (2 <= len(s) <= 6):
        return False

    # Must start with at least two letters
    if not s[0:2].isalpha():
        return False

    # Check for numbers and invalid punctuation
    has_number_started = False
    for i in range(len(s)):
        if not s[i].isalnum():
            return False

        if s[i].isdigit():
            # First number cannot be '0'
            if not has_number_started and s[i] == '0':
                return False
            has_number_started = True

        # If a number has started, letters cannot follow it
        if has_number_started and s[i].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
