text = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

print("Output: ", end="")


for char in text:
    if char not in vowels:
        print(char, end="")

print()
