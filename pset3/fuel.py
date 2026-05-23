while True:
    fuel = input("Fraction: ").strip()
    try:

        numerator, denominator = fuel.split("/")

        x = int(numerator)
        y = int(denominator)
        if 0 <= x <= y and y > 0:
            percentage = round((x / y) * 100)
            break
    except (ValueError, ZeroDivisionError):
        pass

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
