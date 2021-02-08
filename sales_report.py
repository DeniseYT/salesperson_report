"""Generate sales report showing total melons each salesperson sold."""

# Version 1 - List

# create empty lists for collecting data seperately.
salespeople = []
melons_sold = []

# import data from another file, collect them by each salesperson in each list. 
f = open('sales-report.txt')
for line in f:
    line = line.rstrip() # remove trailing whitesapce.
    entries = line.split('|') # create list to store data (remove | ) 

    # print(entries) # each salesperson info stores in each list seperatly.

    salesperson = entries[0] # clarify list index 0 is salesperson.
    melons = int(entries[2]) # clarify list index 2 is melons sold.

    if salesperson in salespeople: # if that salesperson is already in the empty list.
        position = salespeople.index(salesperson) # check that salesperson is in which index.

        melons_sold[position] += melons # increment melon he sold.
    else:
        salespeople.append(salesperson) # if that salesperson is not in the list yet.
        melons_sold.append(melons) # add melon he sold.
    
 
for i in range(len(salespeople)): # check salespeople list from the begining to the end.
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') # print each salesperson's name and number of melon he sold total.


# Version 2 - Dictionary

# create an empty dic to store data
sales_report = {}

