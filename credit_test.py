import credit
import random

daysInMonth = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

#Tester code to try to test the code.
#Separate from the tester code found in credit.py
#No tests created as of oct7.
#idea: one section manually tests specific instances, and another section tries random valid entries.

#return a real possible day given the month and year.
def randomDay(month, year):
    last_day_in_month = daysInMonth[month]
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        last_day_in_month = 29
    return random.randint(1,last_day_in_month)



if __name__ == '__main__':
    print(randomDay(1,2020))
    #tests for "date_same_or_later(day1, month1, day2, month2)" function
    #credit.date_same_or_later()