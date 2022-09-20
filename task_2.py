date = input().split(".")

day = int(date[0])
month = int(date[1])
year = int(date[2])

days_in_month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31,\
'6': 30, '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

def check_leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        days_in_month['2'] = 29

def check_month(month):
    if 1 <= month <= 12:
        pass
    else:
        print("Такой даты нет!")
        exit()

def check_day(day):
    test_date = days_in_month.get(str(month))
    if 1 <= day <= test_date:
        pass
    else:
        print("Такой даты нет!")
        exit()

check_leap_year(year)
check_month(month)
check_day(day)