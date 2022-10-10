from multiprocessing import set_start_method
import credit
import random
import math

num_of_tests_passed = 0
num_of_tests = 0


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
        amount = randomAmount(credit.amount_owed(day, month)) 
        credit.purchase(amount, day, month, country)
        credit.pay_bill(amount, day, month)
    if starting_cur == credit.amount_owed(day, month):
        return True
    return False

#test the intialize() function
def test_intialize():
    #arbitrarily messing with the variables
    credit.cur_balance_owing_intst = math.pi
    credit.cur_balance_owing_intst += 1.4
    credit.cur_balance_owing_recent = 1234
    credit.last_country = "among us"
    credit.last_country2 = "sussy sus"
    credit.last_update_day = 4321
    credit.last_update_month = 7890
    #this variable may be named something different.
    credit.card_disabled = True
    credit.MONTHLY_INTEREST_RATE = 9999
    credit.initialize()
    if credit.cur_balance_owing_intst != 0:
        return False
    if credit.cur_balance_owing_recent != 0:
        return False
    if credit.last_country != None or credit.last_country == "among us":
        return False
    if credit.last_country2 != None or credit.last_country2 == "sussy sus":
        return False
    if credit.last_update_day != -1:
        return False
    if credit.last_update_month != -1:
        return False
    if credit.card_disabled != False:
        return False
    if credit.MONTHLY_INTEREST_RATE != 0.05:
        return False

#test the date_same_or_later() function. Prints outputs, must be checked manually. 
def test_date_same_or_later(num_of_trials):
    for x in range(num_of_trials):
        randMonth = random.randint(1,12)
        randDay = randomDay(randMonth, 2020)
        randMonth2 = random.randint(1,12)
        randDay2 = randomDay(randMonth, 2020)
        print(randDay, randMonth, randDay2, randMonth2, credit.date_same_or_later(randDay, randMonth, randDay2, randMonth2))

#test the purchase function at any given time. 
# Arbitrarily max 500 purchase amount and 'Venezuela'
# May cause "error" if the chosen random day is before previous actions.
def test_purchase():
    randMonth = random.randint(1,12)
    randDay = randomDay(randMonth, 2020)
    country = "Venezuela"
    max_amount = 500
    owed_already = credit.amount_owed(randDay, randMonth)
    purchase_amount = randomAmount(max_amount)
    if credit.purchase(purchase_amount, randDay, randMonth, country) == "error":
        return 'error'
    #print(credit.amount_owed(randDay, randMonth), purchase_amount, owed_already)
    if credit.amount_owed(randDay, randMonth) == owed_already + purchase_amount:
        
        return True
    return False

#test the amount_owed function. Initializes credit.
def test_amount_owed():
    credit.initialize()
    if credit.amount_owed(2, 1) != 0:
        print(1)
        return False
    if credit.amount_owed(1, 1) != 'error':
        print(2)
        return False
    credit.initialize()
    expected_amount = randomAmount(500)
    credit.purchase(expected_amount, 1, 1, "Canada")
    if credit.amount_owed(randomDay(1, 2020),1) != expected_amount:
        print(3)
        return False
    if credit.amount_owed(1, 2) != expected_amount:
        print(4)
        return False
    if credit.purchase(456, 1, 2, "Canada") == 'error':
        print(5)
        return False
    if credit.amount_owed(randomDay(2, 2020), 2) != expected_amount + 456:
        print(6)
        return False
    if credit.amount_owed(1, 3) != expected_amount*1.05 + 456:
        print(7)
        return False
    if credit.purchase(312, 31, 3, "Canada") == 'error':
        print(8)
        return False
    if credit.amount_owed(1, 5) != ((expected_amount*1.05 + 456)*1.05 + 312)*1.05:
        print(9)
        return False
    if credit.pay_bill(200, 1, 5) == 'error':
        print(10)
        return False
    if credit.purchase(98, 31, 5, "Canada") == 'error':
        print(11)
        return False
    if credit.amount_owed(1,6) != (((expected_amount*1.05 + 456)*1.05 + 312)*1.05 - 200)*1.05 + 98:
        print(12)
        return False
    return True


if __name__ == '__main__':
    print(test_amount_owed())
    print(test_purchase())
    #credit.purchase(300, 1, 1, "Canada")
    #print(credit.amount_owed(1,1))
    credit.initialize()
    print(buyAndPay(1, 1, "Canada", 100))
    #test_date_same_or_later(10)