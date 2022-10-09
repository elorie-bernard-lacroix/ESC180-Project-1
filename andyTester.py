from ast import Return
from symbol import return_stmt
from tkinter.tix import Tree
import credit

numOfTestsPassed = 0

# regular purchase (1 /month), pays back at beginning of next month
#print("TEST CASE 1")
def test1():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    if (credit.amount_owed(31, 1)) != 80: #80.0
        return False
    credit.pay_bill(80, 1, 2)
    credit.purchase(80, 1, 2, "Canada")
    if (credit.amount_owed(29, 2)) != 80:
        return False  # 80.0
    credit.pay_bill(80, 1, 3)
    credit.purchase(80, 1, 3, "Canada")
    if (credit.amount_owed(31, 3)) != 80:
        return False  # 80.0
    return True


# regular purchase (1 /month), pays half at beginning of next month
#print("TEST CASE 2")
def test2():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    if (credit.amount_owed(31, 1)) != 80:
        return False  # 80.0
    credit.pay_bill(40, 1, 2)  # 40
    credit.purchase(80, 1, 2, "Canada")  # 120 (40 + 80)
    if (credit.amount_owed(29, 2)) != 120:
        return False  # 120.0 (40 interest, 80 non-interest)
    if round(credit.amount_owed(1, 3), 5) != 122:
        return False  # 122.0 (40*1.05+80 interest, 0 non-interest)
    credit.pay_bill(40, 1, 3)  # 82.0 (82 interest, 0 non-interest)
    credit.purchase(80, 1, 3, "Canada")  # 162.0 (82 interest, 80 non-interest)
    if round(credit.amount_owed(31, 3), 5) != 162:
        return False  # 162.0 (82 interest, 80 non-interest)
    if round(credit.amount_owed(1, 4), 5) != 166.1:
        return False  # 166.1 (86.1+80 interest, 0 non-interest)
    return True
# regular purchase (2 /month), pays back at beginning of next month
#print("TEST CASE 3")
def test3():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "Canada")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    #if round(credit.amount_owed(31, 1))  # 80.0
    credit.pay_bill(160, 1, 2)
    credit.purchase(80, 1, 2, "Canada")
    credit.purchase(80, 2, 2, "Canada")
    if round(credit.amount_owed(29, 2), 5) != 160:
        return False
    #if round(credit.amount_owed(29, 2))  # 80.0
    credit.pay_bill(160, 1, 3)
    credit.purchase(80, 1, 3, "Canada")
    credit.purchase(80, 2, 3, "Canada")
    if round(credit.amount_owed(31, 3), 5) != 160:
        return False
    #if round"Now owing:", credit.amount_owed(31, 3))  # 80.0
    return True
# regular credit.purchase (2 /month), pays half at beginning of next month
#print("TEST CASE 4")
def test4():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "Canada")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    #if round"Now owing:", credit.amount_owed(31, 1))  # 160.0
    credit.pay_bill(80, 1, 2)  # 80
    credit.purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    credit.purchase(80, 2, 2, "Canada")
    if round(credit.amount_owed(29, 2), 5) != 240:
        return False
    if round(credit.amount_owed(1, 3), 5) != 244:
        return False
    #if round"Now owing:", credit.amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    #if round"Now owing:", credit.amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    credit.pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    credit.purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    credit.purchase(80, 2, 3, "Canada")
    if round(credit.amount_owed(31, 3), 5) != 324:
        return False
    if round(credit.amount_owed(1, 4), 5) != 332.2:
        return False
    #if round"Now owing:", credit.amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    #if round"Now owing:", credit.amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)
    return True
# buy once, pay in june in full, check in december
#print("TEST CASE 5")
def test5():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    if round(credit.amount_owed(15, 6), 5) != 97.2405:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    credit.pay_bill(97.24050000000001, 15, 6)
    if round(credit.amount_owed(15, 6), 5) != 0:
        return False
    if round(credit.amount_owed(31, 12), 5) != 0:
        return False

    #if round"Now owing:", credit.amount_owed(15, 6))
    #if round"Now owing:", credit.amount_owed(31, 12))
    return True
# buy once, pay in june in partial, check in december
#print("TEST CASE 6")
def test6():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    if round(credit.amount_owed(15, 6), 5) != 97.2405:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    credit.pay_bill(10, 15, 6)  # 87.2405 remaining
    if round(credit.amount_owed(15, 6), 5) != 87.2405:
        return False
    if round(credit.amount_owed(31, 12), 5) != 116.91061:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # 87.2405->91.602525(july)->96.18265125->100.9917838125->106.0413730031->
    #if round"Now owing:", credit.amount_owed(31, 12))  # 111.3434416533 in november -> 116.9106137359 in december
    return True
# buy once, buy again in early june, pay in june in full for jan debt+interest, check in december
#print("TEST CASE 7")
def test7():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 1, 6, "Canada")
    if round(credit.amount_owed(15, 6), 5) != 97.2405+80:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    credit.pay_bill(97.2405, 15, 6)  # 80 new debt remaining
    if round(credit.amount_owed(15, 6), 5) != 80:
        return False
    if round(credit.amount_owed(31, 12), 5) != 102.10253:
        return False
    return True
    #if round"Now owing:", credit.amount_owed(15, 6))  # 80
    #if round"Now owing:", credit.amount_owed(31, 12))  # 80->80->84->88.2->92.61->97.2405->102.102525

# buy once, buy again in early june, pay in june (slightly more than jan debt+interest), check in december
#print("TEST CASE 8")
def test8():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 1, 6, "Canada")
    if round(credit.amount_owed(15, 6), 5) != 177.2405:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    credit.pay_bill(100, 15, 6)  # 77.2405 (all new debt) remaining
    if round(credit.amount_owed(15, 6), 5) != 77.2405:
        return False
    if round(credit.amount_owed(31, 12), 5) != 98.58063:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))
    #if round"Now owing:", credit.amount_owed(31, 12))  # 77.2405->77.2405->81.102525->85.15765125
# ->89.4155338125->93.8863105031->98.5806260283 (at dec)
    return True
# buy once, buy again in early june, pay in june (slightly less than jan debt+interest), check in december
#print("TEST CASE 9")
def test9():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 1, 6, "Canada")
    if round(credit.amount_owed(15, 6), 5) != 177.2405:
        return False
    #if round"Now owing:", credit.amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    credit.pay_bill(90, 15, 6)  # 87.2405 remaining (7.2405 old debt)
    if round(credit.amount_owed(15, 6), 5) != 87.2405:
            return False
    if round(credit.amount_owed(31, 12), 5) != 111.80549:
            return False
    #if round"Now owing:", credit.amount_owed(15, 6))
    #if round"Now owing:", credit.amount_owed(31, 12))  # 80+7.2405(june)->80+7.602525 (87.602525)->91.98265125->96.5817838125
    # ->101.4108730031->106.4814166533->111.805487486
    return True
# buy once, forget about the card
#print("TEST CASE 10")
def test10():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    if round(credit.amount_owed(31, 12), 5) != round(80*(1.05**10), 5):
        return False
    #if round"Now owing:", credit.amount_owed(31, 12))  # 80->80(feb)->(80*1.05^10)(dec)130.3115701422
    return True
# buy once, pay back immediately forget about the card
#print("TEST CASE 11")
def test11():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.pay_bill(80, 1, 1)
    if round(credit.amount_owed(31, 12), 5) != 0:
        return False
    #if round"Now owing:", credit.amount_owed(31, 12))  # 0
    return True
# TEST 4 but with alternating 2 countries
#print("TEST CASE 12")
def test12():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "France")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    credit.pay_bill(80, 1, 2)  # 80
    credit.purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    credit.purchase(80, 2, 2, "France")
    if round(credit.amount_owed(29, 2), 5) != 240:
        return False
    if round(credit.amount_owed(1, 3), 5) != 244:
        return False
    credit.pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    credit.purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    credit.purchase(80, 2, 3, "France")
    if round(credit.amount_owed(31, 3), 5) != 324:
        return False
    if round(credit.amount_owed(1, 4), 5) != 332.2:
        return False
    return True
# TEST 4 but with alternating 3 countries
#print("TEST CASE 13")
def test13():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "France")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    credit.pay_bill(80, 1, 2)  # 80 interest building debt
    if credit.purchase(80, 1, 2, "China") != 'error':
        return False # FRAUD - ERROR, still 80
    if credit.purchase(80, 2, 2, "France") != 'error':
        return False  # ALREADY FRAUD - ERROR, still 80
    if round(credit.amount_owed(29, 2), 5) != 80:
        return False
    if round(credit.amount_owed(1, 3), 5) != 84:
        return False
    credit.pay_bill(80, 1, 3)  # 4.0 (4 interest, 0 non-interest)
    if credit.purchase(80, 1, 3, "Canada") != 'error':
        return False # ALREADY FRAUD - ERROR, still 4
    if credit.purchase(80, 2, 3, "France") != 'error':
        return False  # ALREADY FRAUD - ERROR, still 4
    if round(credit.amount_owed(31, 3), 5) != 4:
        return False
    if round(credit.amount_owed(1, 4), 5) != 4.2:
        return False
    return True

# TEST 4 but with same country -> then 2 other countries
#print("TEST CASE 14")
def test14():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "Canada")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    credit.pay_bill(80, 1, 2)  # 80
    credit.purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    credit.purchase(80, 2, 2, "Canada")
    if round(credit.amount_owed(29, 2), 5) != 240:
        return False
    if round(credit.amount_owed(1, 3), 5) != 244:
        return False
    credit.pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    credit.purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    if credit.purchase(80, 2, 3, "France") != 'error':
        return False  # FRAUD, STILL 244 (164 interest, 80 non-interest)
    if round(credit.amount_owed(2, 3), 5) != 244:
        return False
    if round(credit.amount_owed(1, 4), 5) != 252.2:
        return False
    return True

# TEST 4 but with 3 countries, but each country credit.purchase twice
#print("TEST CASE 15")
def test15():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(80, 2, 1, "Canada")
    if round(credit.amount_owed(31, 1), 5) != 160:
        return False
    credit.pay_bill(80, 1, 2)  # 80
    credit.purchase(80, 1, 2, "France")  # 160 (80 + 80)
    credit.purchase(80, 2, 2, "France")
    if round(credit.amount_owed(29, 2), 5) != 240:
        return False
    if round(credit.amount_owed(1, 3), 5) != 244:
        return False    
    credit.pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    credit.purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    credit.purchase(80, 2, 3, "China")
    if round(credit.amount_owed(31, 3), 5) != 324:
        return False
    if round(credit.amount_owed(1, 4), 5) != 332.2:
        return False
    return True

# Fraud early on, but don't pay back
#print("TEST CASE 16")
def test16():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(50, 2, 1, "France")
    credit.purchase(30, 2, 1, "Germany")
    credit.purchase(30, 3, 1, "Germany")
    if round(credit.amount_owed(31, 1), 5) != 130:
        return False  # 0
    if round(credit.amount_owed(31, 2), 5) != 130:
        return False
    if round(credit.amount_owed(31, 3), 5) != 130*1.05:
        return False
    if round(credit.amount_owed(31, 12), 5) != round(130*(1.05**10), 5):
        return False
    return True

# Fraud early on, but pay back
#print("TEST CASE 17")
def test17():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(50, 2, 1, "France")
    credit.purchase(30, 2, 1, "Germany")
    credit.purchase(30, 3, 1, "Germany")
    credit.pay_bill(130, 3, 1)
    if round(credit.amount_owed(31, 1), 5) != 0:
        return False  # 0
    if round(credit.amount_owed(31, 2), 5) != 0:
        return False
    if round(credit.amount_owed(31, 3), 5) != 0:
        return False
    if round(credit.amount_owed(31, 12), 5) != 0:
        return False
    return True
# Fraud early on, but pay back
#print("TEST CASE 18")
def test18():
    credit.initialize()  # reset the code
    credit.purchase(80, 1, 1, "Canada")
    credit.purchase(50, 2, 2, "France")
    credit.pay_bill(90, 3, 2)  # now owe 40 non interest
    credit.purchase(30, 3, 3, "Germany")
    credit.purchase(30, 4, 4, "Germany")
    if round(credit.amount_owed(31, 3), 5) != 40:
        return False  # 40 interested money
    if round(credit.amount_owed(31, 12), 5) != round(40*(1.05**9), 5):  # 40*1.05**9
        return False
    return True

if test1():
    numOfTestsPassed += 1
else:
    print(1)
if test2():
    numOfTestsPassed += 1
else:
    print(2)
if test3():
    numOfTestsPassed += 1
else:
    print(3)
if test4():
    numOfTestsPassed += 1
else:
    print(4)
if test5():
    numOfTestsPassed += 1
else:
    print(5)
if test6():
    numOfTestsPassed += 1
else:
    print(6)
if test7():
    numOfTestsPassed += 1
else:
    print(7)
if test8():
    numOfTestsPassed += 1
else:
    print(8)
if test9():
    numOfTestsPassed += 1
else:
    print(9)
if test10():
    numOfTestsPassed += 1
else:
    print(10)
if test11():
    numOfTestsPassed += 1
else:
    print(11)
if test12():
    numOfTestsPassed += 1
else:
    print(12)
if test13():
    numOfTestsPassed += 1
else:
    print(13)
if test14():
    numOfTestsPassed += 1
else:
    print(14)
if test15():
    numOfTestsPassed += 1
else:
    print(15)
if test16():
    numOfTestsPassed += 1    
else:
    print(16)
if test17():
    numOfTestsPassed += 1
else:
    print(17)
if test18():
    numOfTestsPassed += 1
else:
    print(18)
print("tests passed:",numOfTestsPassed)