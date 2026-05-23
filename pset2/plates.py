def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1 & 2: Length check and starts with two letters
    if not (2 <= len(s) <= 6) or not s[0:2].isalpha():
        return False

    # Rule 4: Must be alphanumeric (no spaces/punctuation)
    if not s.isalnum():
        return False

    # Rule 3: Check numbers handling
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0':
                return False
            if not s[i:].isdigit():
                return False
            break

    return True

if __name__ == "__main__":
    main()
