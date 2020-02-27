def totalpaid(cost,paid):
    #Checking to ensure that the values entered are numerical. Converts them to float numbers if so.
    try:
        cost = float(cost)
        paid = float(paid)
        #check to ensure the amount paid is greater than the cost
    except:
        print("Please enter in a number value.")

    dollars = 0    
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0    
        
    #Finds the amount of change based on the amount paid subtracted from the total amount, rounded to two places
    change = round(paid - cost,2)
    #Uses the number preceding the decimal 
    dollars = int(change)
    #subtracts the dollars from the total change to get the amount of cents remaining, rounded to two places
    cents = round(change - dollars,2)
    remaining_change = cents
    
    #following sequence checks to see if there's enough change for each type of coin. If so, it subtracts from the running total
    if cents/.25 >= 1:
        quarters = int(cents/.25)
        remaining_change = round(cents - (quarters*.25),2)
    
    if remaining_change/.1 >= 1:
        dimes = int(remaining_change/.1)
        remaining_change = round(remaining_change - (dimes*.1),2)
    
    if remaining_change/.05 >=1:
        nickels = int(remaining_change/.05)
        remaining_change = round(remaining_change - (nickels*.05),2)
    
    if remaining_change/.01 >=1:
        pennies = int(remaining_change/.01)
        remaining_change = round(remaining_change - (pennies *.01),2)
        
    print(f"The total was ${cost}. The customer paid ${paid}. \n\n Amount Due: \n Dollars: {dollars} \n Quarters: {quarters} \n Dimes: {dimes} \n Nickels: {nickels} \n Pennies: {pennies} ")
 

#    
#Asks for cost and amount paid
#Removes leading dollar sign, if any, to convert input to float
#Runs totalpaid function to calculate change needed
#    
item_cost = input("What did the item cost?")
if item_cost[0] == '$':
    item_cost = item_cost.replace('$','')
item_cost = float(item_cost)

amount_paid = input("How much did the customer pay?")
if amount_paid[0] == '$':
    amount_paid = amount_paid.replace('$','')
amount_paid = float(amount_paid)

totalpaid(item_cost,amount_paid)
