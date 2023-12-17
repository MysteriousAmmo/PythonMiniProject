'''
The threshold for the words is a bit lower (2) just for testing, please increase it. 
'''


def descsplit(x, y, descdict):
    # Continuously prompt the user for input until they type 'exit'
    while y.lower() != 'exit':
        print("Type 'exit' to stop entering")
        
        # Split the description into a list of unique words
        templist = x.split()
        templist1 = list(set(templist))
        templist1.sort()
        
        # Associate the expenditure name with the list of words in the dictionary
        descdict[y] = templist1
        
        # Prompt the user for the next expenditure name and description
        y = input("Enter the expenditure name: ")
        x = input("Enter a short description of the item: ")
    
    return descdict

def categorize_items(item_dict):
    word_count_dict = {}
    item_category_dict = {}

    # Iterate through each item and its associated description
    for item, description in item_dict.items():
        # Count the occurrences of each word in all descriptions
        for word in description:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    # Identify words that occur two or more times as potential categories
    for word, count in word_count_dict.items():
        if count >= 2:
            category_name = word
            # Categorize items based on words occurring two or more times
            item_category_dict[category_name] = [item for item, desc in item_dict.items() if word in desc]

    return item_category_dict

def main():
    item_dict = {}
    
    # Prompt the user to enter the first item's description and expenditure name
    descin = input("Enter a short description of the item: ")
    namein = input("Enter the expenditure name: ")
    
    # Call the function to collect item names and descriptions until 'exit'
    item_dict = descsplit(descin, namein, item_dict)

    # Call the function to categorize items based on common words
    category_dict = categorize_items(item_dict)

    # Display the categorized items
    print("\nCategories:")
    for category, items in category_dict.items():
        print(f"{category}: {', '.join(items)}")

if __name__ == "__main__":
    main()
