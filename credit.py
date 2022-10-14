"""
Last modified on 2022-10-11 by Elorie Bernard-Lacroix and Chaewon Lim
"""

def initialize():
    '''This function initializes all global variables.'''
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global card_disabled
    global MONTHLY_INTEREST_RATE

    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None 

    card_disabled = False   
    
    MONTHLY_INTEREST_RATE = 0.05

def date_same_or_later(day1, month1, day2, month2):
    '''This function accepts 4 input variables: (day1, month1) and (day2, month2) as integers, where
    both dates are valid dates (for example, (01, 02, 22, 10)). 
    
    It will return True if the date (day1, month1) is the same as the date (day2, month2), 
    or occurs later than (day2, month2).'''

    if month1 > month2:
        return True

    if month1 == month2:
        if day1 >= day2:
            return True
        return False

    return False

    
def all_three_different(c1, c2, c3):
    '''This function accepts 3 strings as inputs: c1, c2, and c3.
    
    It will return True if the values of the three strings are all different.'''

    if c1 != c2 and c2 != c3 and (c3 != c1 and c3 != None):
        return True

    return False
        
    
        
def purchase(amount, day, month, country):
    '''
    This function simulates a purchase, updating the 'cur_balance_owing_recent' value. 
    
    It accepts the inputs of purchase amount ('amount'), date of purchase (day, month as integers), 
    and country of the purchase ('country' given as a capitalized string). 
    
    It will return 'error' and not execute the purchase if:
    - the card is disabled
    - there has been three consecutive purchases in different countries (this will also disable the card)
    - there has been an update to the account on the same day or later
    '''
    
    global cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global card_disabled

    # return 'error' if card is disabled
    if card_disabled:
        return 'error'

    # disable card and return 'error' if there have been three consecutive different country purchases    
    if all_three_different(country, last_country, last_country2):
        card_disabled = True
        return 'error'
    
    # return 'error' if the purchase date is before the last update date
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    
    # update the current interest owed, if appropriate
    check_new_month(month)

    # update record of country
    last_country2 = last_country
    last_country = country

    # update variables with dates
    last_update_day = day
    last_update_month = month

    # process payment and add it to the current amount owed
    cur_balance_owing_recent += amount        


# Simulate checking how much money is owed.
# Return the amount owed.
def amount_owed(day, month):
    global last_update_day
    global last_update_month
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    # check if it's a new month
    check_new_month(month)
    
    #update variables with dates
    last_update_day = day
    last_update_month = month

    return cur_balance_owing_intst + cur_balance_owing_recent

# checks if the simulation function occurs in a new month, and adds the appropriate interest.    
def check_new_month(month):
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    # initially considers for the first month that passes, then adds (or rather, multiplies) the subsequent interests 
    if month > last_update_month:
        cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE)
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_intst *= (1 + MONTHLY_INTEREST_RATE)**(month - last_update_month -1)
        cur_balance_owing_recent = 0

# Simulate paying the bill.
# Unclear what to do about cases where the amount is bigger than the owed.
# Return 'error' for now, but maybe there is specific instruction.   
def pay_bill(amount, day, month):
    # First check if the day is valid and return 'error' if needed.
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    global last_update_day
    global last_update_month
    # First check if the day is valid and return 'error' if needed.
    # Because this depends on last_update_day and last_update_month, every simulation
    # function MUST update last_update_day and last_update_month.
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return 'error'
    
    # Calculate and store the new balances.
    #cannot pay an amount more than is owed.
    if amount > cur_balance_owing_intst + cur_balance_owing_recent:
        return 'error'
    # check if it's a new month
    check_new_month(month)
    if cur_balance_owing_intst - amount >= 0:
        cur_balance_owing_intst -= amount
    else:
        cur_balance_owing_recent += (cur_balance_owing_intst - amount)
        cur_balance_owing_intst = 0
    
    # update variables with dates
    last_update_day = day
    last_update_month = month    

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':
    # Testing the functions
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