# A file containing all callable functions that will likely be called finally 

import csv 
import math 

descin = str(input("Enter a short description of the item")) 
namein = str(input("Enter the expenditure name")) 

def descsplit (x,y): 
    descdict = [] 

    print("Type 'exit' to stop enterring") 

    while y != 'exit': 
        templist = x.split() 
        templist1 = list(set(templist)) 
        templist1.sorted()
        descdict[y] = templist1
        return descdict
    


    

