def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        print("Invalid month!")
        check()
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months_names = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"]

    if is_leap(year) and month == 2:
        return 29
    return f"Total days in {months_names[month-1]} of {year} are '{month_days[month-1]}'"


def check():
    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    days = days_in_month(year, month)
    print(days)


check()
