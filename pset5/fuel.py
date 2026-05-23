def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    parts = fraction.split("/")
    if len(parts) != 2:
        raise ValueError

    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    if x < 0 or y < 0 or x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
