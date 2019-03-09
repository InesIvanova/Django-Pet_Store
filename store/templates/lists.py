from datetime import datetime

EXAM_DATE = datetime(year=2018, month=8, day=26)

year, month, day = list(map(int, input().split('-')))
date = datetime(year=year, month=month, day=day)

if date < EXAM_DATE:
    print('Passed')
elif date == EXAM_DATE:
    print('Today date')
else:
    number_of_days = abs(EXAM_DATE - date)
    print(f'{int(number_of_days.days)+1} days left')