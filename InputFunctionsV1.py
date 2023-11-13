'''
This is all preliminary code, nothing has been tested as of yet, there are many placeholder names. I have tried to indicate with comments wherever this has happened but I might have missed some occurances. Ask me if there is anything which doesnt make sense. 

'''


import csv 
import math 

# Taking value inputs 
# To operate, simply call the function

def intin(n): 
    n = int(input("Enter the value of the item in Rupees: ")) 

    return n 


# Taking item name inputs
# To operate, simply call the function

def strin(s): 
    s = str(input("Enter the item/service name: ")) 

    return s


# Inputing single value and item name inputs into a dictionary.
# The strin and intin functions have to be called prior to calling this function, otherwise the 'n' and 's' variables will have no values.
# To operate, first call the intin and strin functions to get values for 'n' and 's', then call this function 

tempdict1 = {} # this line is required only once and is not part of this code set

def dictin1(): 
    tempdict1[n] = s 




# Inputting multiple value and item name inputs into a dictionary at once. 
# The function is self sufficient (does not need other functions to be called prior to operation). 
# To operate simply call the function and type exit when done inputting values. 

tempdict2 = {} # this line is required only once and is not part of this code set

def dictin2(): 

    n = ''
    s = 0

    print("type 'exit' once done inputting new items") 

    while n != 'exit': 
        intin(n) 
        strin(s) 

        tempdict2[n] = s 

    

# Opening CSV file to store everything (first open) - Possibly unnecessary 

def firstopen(f): 
    with open(tempfilename, 'w') as csvfile: 
        csvwriter = csv.writer(csvfile) 

        writer.writeheader() 

        writer.writerows(tempdict) 




# Initializing the dictionary to be written to later (not a function since this will likely only be done once) 


fields = ['Item/Service', 'Value/Spending'] 

# the content of the fields variable is something to be decided in a group discussion, therefore placeholders are used for now 

with open(tempfilename, 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 




# Finding the expenditure per month 

Total = 0

def total (): 
    total = 0
    for element in tempdict2.values():
        total = total + element 

    return (total) 

    
    
