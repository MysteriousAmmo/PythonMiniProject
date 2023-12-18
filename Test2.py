def descsplit(x, y, descdict):
    while y.lower() != 'exit':
        print("Type 'exit' to stop entering")
        templist = x.split()
        templist1 = list(set(templist))
        templist1.sort()
        descdict[y] = templist1
        y = input("Enter the expenditure name: ")
        x = input("Enter a short description of the item: ")
    return descdict

def categorize_items(item_dict):
    word_count_dict = {}
    item_category_dict = {}

    for item, description in item_dict.items():
        for word in description:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    for word, count in word_count_dict.items():
        if count >= 3:  # Adjust this to be higher
            category_name = word
            item_category_dict[category_name] = [item for item, desc in item_dict.items() if word in desc]

    return item_category_dict

def main():
    item_dict = {}
    descin = input("Enter a short description of the item: ")
    namein = input("Enter the expenditure name: ")
    item_dict = descsplit(descin, namein, item_dict)

    category_dict = categorize_items(item_dict)

    print("\nCategories:")
    for category, items in category_dict.items():
        print(f"{category}: {', '.join(items)}")

if __name__ == "__main__":
    main()
