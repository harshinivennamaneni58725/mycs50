def main():
    answer = input("what is the answer to the great question of life, the universe, and everything? ")
    clean_answer = answer.strip().lower()
    if clean_answer == "42" or clean_answer == "forty-two" or clean_answer == "forty two":
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()
