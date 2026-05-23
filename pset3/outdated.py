months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_str = input("Date: ").strip()

    if "/" in date_str:
        try:
            parts = date_str.split("/")
            if len(parts) == 3:
                month = int(parts[0])
                day = int(parts[1])
                year = int(parts[2])


                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        except ValueError:
            pass

    elif "," in date_str:
        try:

            left_part, year_part = date_str.split(",")
            year = int(year_part.strip())

            month_name, day_str = left_part.strip().split(" ")
            day = int(day_str)

            if month_name in months:
                month = months.index(month_name) + 1

                if 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
        except ValueError:
            pass
