date = input().split(".")
day = int(date[0])
month = int(date[1])
year = int(date[2])

def check_date(day, month, year):
    days_in_month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31,\
    '6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        days_in_month['2'] = 29
    test_date = days_in_month.get(str(month))
    if 1 <= month <= 12:
        if 1 <= day <= test_date:
            return True
        else:
            return False
    else:
        return False

print(check_date(day, month, year))
