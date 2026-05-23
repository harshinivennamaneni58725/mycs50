def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    shortened = ""
    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            shortened += char
    return shortened


if __name__ == "__main__":
    main()
