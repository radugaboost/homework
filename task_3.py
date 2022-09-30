notes = ["завтра 20 января 2033 года, меня наконец то отчислят",
             "меня снова не отчислили",
             "новый день, до попытки отчисления осталось 364 дня"]
start_date = '19.01.2033'

from datetime import timedelta, date

def captain(notes, start_date):
    file = open('captain_notes', 'w')
    start_date = [int(i) for i in start_date.split('.')]
    cur_date = date(start_date[2], start_date[1], start_date[0])
    for days in range(len(notes)):
        file.writelines(str(cur_date + timedelta(days)) + ' ' + notes[days] + '\n')
    file.close()

captain(notes, start_date)
