"""The Credit Card Simulator starter code
You should complete every incomplete function,
and add more functions and variables as needed.
Ad comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Oct. 3, 2022
"""

# You should modify initialize()
def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None    
    
    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    pass
    
def all_three_different(c1, c2, c3):
    pass
        
    
        
def purchase(amount, day, month, country):
    pass


# Simulate checking how much money is owed.
# Return the amount owed.
def amount_owed(day, month):
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    return cur_balance_owing_intst + cur_balance_owing_recent
    

# Simulate paying the bill.
# Unclear what to do about cases where the amount is bigger than the owed.
# Return 'error' for now, but maybe there is specific instruction.   
def pay_bill(amount, day, month):
    # First check if the day is valid and return 'error' if needed.
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    global last_update_day
    global last_update_month
    # Because this depends on last_update_day and last_update_month, every simulation
    # function MUST update last_update_day and last_update_month.
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    # Calculate and store the new balances.
    #cannot pay an amount more than is owed.
    if amount > cur_balance_owing_intst + cur_balance_owing_recent:
        return 'error'
    if cur_balance_owing_intst - amount >= 0:
        cur_balance_owing_intst -= amount
    else:
        cur_balance_owing_recent += (cur_balance_owing_intst - amount)
        cur_balance_owing_intst = 0
    last_update_day = day
    last_update_month = month    

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':
    # Describe your testing strategy and implement it below.
    # What you see here is just the simulation from the handout, which
    # doesn't work yet.
    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375 
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in 
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375 
                                                # (43.65375*1.05+40)
                                            
                                            
    