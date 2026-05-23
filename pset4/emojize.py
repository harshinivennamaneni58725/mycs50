import emoji


def main():
    user_input = input("Input: ")
    print("Output:", emoji.emojize(user_input, language="alias"))


if __name__ == "__main__":
    main()
