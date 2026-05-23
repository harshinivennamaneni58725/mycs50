def main():
    answer = input("What time is it? ").strip()

    hours = convert(answer)

    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")


def convert(time):

    if "a.m." in time or "p.m." in time:
        time, period = time.split(" ")
        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)

        if period == "p.m." and hours != 12:
            hours += 12
        elif period == "a.m." and hours == 12:
            hours = 0
    else:

        hours, minutes = time.split(":")
        hours = float(hours)
        minutes = float(minutes)

    return hours + (minutes / 60.0)


if __name__ == "__main__":
    main()

