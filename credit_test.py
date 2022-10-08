from multiprocessing import set_start_method
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

#idea: one section manually tests specific instances, and another section tries random valid entries.

#return a real possible day given the month and year.
def randomDay(month, year):
    last_day_in_month = daysInMonth[month]
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
        last_day_in_month = 29
    return random.randint(1,last_day_in_month)

#return a real possible amount
def randomAmount(upper_bound):
    return round((random.random() * upper_bound), 2)

# Simulate buying and paying back some random amount immediately n times in the same country on the same day.
# Return true iff the amount owed does not change.
def buyAndPay(day, month, country, n):
    starting_cur = credit.amount_owed(day, month)
    for i in range(n):
        amount = randomAmount(credit.amount_owed()) 
        credit.purchase(amount, day, month, country)
        credit.pay_bill(amount, day, month, country)
    if starting_cur == credit.amount_owed(day, month):
        return True
    return False


if __name__ == '__main__':
    print(randomDay(1,2020))
    #tests for "date_same_or_later(day1, month1, day2, month2)" function
    #credit.date_same_or_later()