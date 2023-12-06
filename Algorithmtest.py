
#descriptions stored as a dictionary containing expenditure name and a list containing the string description split into a list of strings.
# Common word ignorance is not yet implemented. 


stringin = str(input("Enter a short description of the item")) 
namein = str(input("Enter the expenditure name")) 
descdict = [] 

# the string input is passed as the argument to the function as 'x' and the item name is passed as 'y'
def descsplit (x,y): 
    while x != 'end':
        print("Type 'end' to stop inputting values, otherwise input item name followed by description")
        y = int(input)
        templist = x.split() 
        descdict[y] = templist 
        return descdict



tempdict1 = descsplit(stringin, namein) 

# Filtering through the desciption to find the words which occur the most. 

wordtemp = []
wordcountdict = []
tempwordindex = []
wordindict = []
itemlist = []


'''
Description of what the following code does: 

1) It takes each entry from the original list of items
2) It splits each item into a key and value through tuple unpacking
3) Then it iterates through each word in the value of the dictionary (original iteration) 
4) For each word, a second iteration through all the items in dictionary is done (second iteration)
5) It then checks if the word from the original iteration occurs in the value string occurs in the second iteration
6) Through the second iteration it stores the count of how many times a word occurs
7) How many times each word occurs along with the word itself is stored in a temp dict
'''
for description in tempdict1.items(): # Step 1
    count = 0 
    key, value = description # Step 2
    for word in value: # Step 3
        for item in tempdict1.items(): # Step 4
            key1, value1, = item
            if word in value1: # Step 5
                count += 1 # Step 6
                wordmain = word
                itemlist.append(key1)
        
        # final count of the word is available at this point, along with confirmation if the word occurs multiple times
        wordtemp[word] = count # Step 7

        tempwordindex[wordmain] = itemlist


for items in wordtemp.items(): 
    key, value = items      
    if value >= 4: 
        #shifts only the words which occur three or more times from the temp dict to the main dict
        wordcountdict[key] = (value-1)  
        #stores the same words as the key, but with the value as the items in which it occurs. 
        wordindict[wordmain]
        
    if count > countmain: 
        highcount = key
    countmain = count

    