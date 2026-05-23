def main():
    expression = input("Expression: ").strip()
    x, y, z = expression.split(" ")

    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z

    print(f"{result:.1f}")

if __name__ == "__main__":
    main()


