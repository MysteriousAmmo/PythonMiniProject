import csv
import tkinter as tk
from tkinter import ttk
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

exp_type_description_dict = {}

def create_exp_dictionary():
    exp_type = exp_entry1.get()
    exp_amount = exp_entry2.get()
    exp_description = exp_description_entry.get()
    essential = checkbox_var1.get()


    exp_data = {
        "Type": exp_type,
        "Amount": exp_amount,
        "Description": exp_description,
        "Essential": essential,
    
    }

    exp_type_description_dict[exp_type] = exp_description


    tree_exp.insert("", tk.END, values=(exp_data["Type"], exp_data["Amount"], exp_data["Description"], exp_data["Essential"]))

    exp_entry1.delete(0, tk.END)
    exp_entry2.delete(0, tk.END)
    exp_description_entry.delete(0, tk.END)
    checkbox_var1.set(False)


def create_income_dictionary():
    income_type = inc_entry1.get()
    income_amount = inc_entry2.get()

    income_data = {
        "Type": income_type,
        "Amount": income_amount
    }

    tree_inc.insert("", tk.END, values=(income_data["Type"], income_data["Amount"]))



    inc_entry1.delete(0, tk.END)
    inc_entry2.delete(0, tk.END)

def delete_expense_item():
    selected_item = tree_exp.selection()
    if selected_item:
        tree_exp.delete(selected_item)

def delete_income_item():
    selected_item = tree_inc.selection()
    if selected_item:
        tree_inc.delete(selected_item)

def save_to_csv():
    with open('expense_income_data.csv', 'w', newline='') as csv_file:
        fieldnames_exp = ["Type", "Amount", "Description", "Essential"]
        writer_exp = csv.DictWriter(csv_file, fieldnames=fieldnames_exp)
        writer_exp.writeheader()
        for item in tree_exp.get_children():
            values = tree_exp.item(item, 'values')
            writer_exp.writerow({fieldnames_exp[i]: values[i] for i in range(len(fieldnames_exp))})

        fieldnames_inc = ["Type", "Amount"]
        writer_inc = csv.DictWriter(csv_file, fieldnames=fieldnames_inc)
        for item in tree_inc.get_children():
            values = tree_inc.item(item, 'values')
            writer_inc.writerow({fieldnames_inc[i]: values[i] for i in range(len(fieldnames_inc))})

def read_from_csv():
    with open('expense_income_data.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if 'Essential' in row:
                tree_exp.insert("", tk.END, values=(row['Type'], row['Amount'], row['Essential']))
            else:
                tree_inc.insert("", tk.END, values=(row['Type'], row['Amount']))

def exp_button():
    save_to_csv()
    create_exp_dictionary()


# # Sample data
# labels = ['Expenditure', 'Savings', 'Investments']
# sizes = [25, 30, 20]

# # Colors for each category
# colors = ['#ff9999', '#66b3ff', '#99ff99']

# # Exploding the 2nd slice (i.e., 'Category B')
# explode = (0, 0.1, 0)

# # Plotting the pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
# plt.title('Simple Pie Chart')
# plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.


# # Show the pie chart
# plt.show()



root = tk.Tk()
root.title("Expense Tracker")
root.configure(bg="black")
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

notebook.add(tab1, text="Expenses")
notebook.add(tab2, text="Income")
notebook.add(tab3, text="Investment")
notebook.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

title = tk.Label(tab1, text="Expense Tracker", font=("Georgia", 60, "bold"), fg="blue")
title.grid(row=0, column=0, padx=50, pady=30, columnspan=2)

exp_label = tk.Label(tab1, text="Expenses", font=("Georgia", 20, "bold"), fg="red")
exp_label.grid(row=1, column=0, padx=10, pady=15, columnspan=2)

exp_entry_label1 = tk.Label(tab1, text="Expense Type:")
exp_entry_label1.grid(row=2, column=0, padx=10, pady=5)
exp_entry1 = tk.Entry(tab1, width=25)
exp_entry1.grid(row=2, column=1, padx=10, pady=5)

exp_entry_label2 = tk.Label(tab1, text="Expense Amount:")
exp_entry_label2.grid(row=3, column=0, padx=10, pady=5)
exp_entry2 = tk.Entry(tab1, width=25)
exp_entry2.grid(row=3, column=1, padx=10, pady=5)

exp_description_label = tk.Label(tab1, text="Description:")
exp_description_label.grid(row=4, column=0, padx=10, pady=5)
exp_description_entry = tk.Entry(tab1, width=25)
exp_description_entry.grid(row=4, column=1, padx=10, pady=5)

exp_checkbox_label = tk.Label(tab1, text="Essential: ")
exp_checkbox_label.grid(row=5, column=0, padx=10, pady=5)

checkbox_var1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(tab1, text="Essential", variable=checkbox_var1)
checkbox1.grid(row=5, column=1, sticky="w")


exp_submit_button = tk.Button(tab1, text="Submit", command=exp_button, fg="white", bg="black")
exp_submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

inc_label = tk.Label(tab2, text="Income", font=("Georgia", 15, "bold"), fg="red")
inc_label.grid(row=1, column=0, padx=10, pady=15, columnspan=2)

inc_entry_label1 = tk.Label(tab2, text="Income Type:")
inc_entry_label1.grid(row=2, column=0, padx=10, pady=5)
inc_entry1 = tk.Entry(tab2, width=25)
inc_entry1.grid(row=2, column=1, padx=10, pady=5)

inc_entry_label2 = tk.Label(tab2, text="Income Amount:")
inc_entry_label2.grid(row=3, column=0, padx=10, pady=5)
inc_entry2 = tk.Entry(tab2, width=25)
inc_entry2.grid(row=3, column=1, padx=10, pady=5)

inc_submit_button = tk.Button(tab2, text="Submit", command=create_income_dictionary, fg="white", bg="black")
inc_submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

columns_exp = ("Type", "Amount", "Description", "Essential")
tree_exp = ttk.Treeview(tab1, columns=columns_exp, show="headings")

for col in columns_exp:
    tree_exp.heading(col, text=col)
    tree_exp.column(col, anchor="center")

tree_exp.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

columns_inc = ("Type", "Amount")
tree_inc = ttk.Treeview(tab2, columns=columns_inc, show="headings")

for col in columns_inc:
    tree_inc.heading(col, text=col)
    tree_inc.column(col, anchor="center")

tree_inc.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

delete_exp_button = tk.Button(tab1, text="Delete Selected", command=delete_expense_item, fg="white", bg="black")
delete_exp_button.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

delete_inc_button = tk.Button(tab2, text="Delete Selected", command=delete_income_item, fg="white", bg="black")
delete_inc_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

save_csv_button = tk.Button(root, text="Save to CSV", command=save_to_csv, fg="white", bg="black")
save_csv_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

exp_entry_label3 = tk.Label(tab3, text='Target savings')
exp_entry_label3.grid(row=3, column=0, padx=10, pady=5)
exp_entry3 = tk.Entry(tab3, width=25)
exp_entry3.grid(row=3, column=1, padx=10, pady=5)
 

title = tk.Label(tab3, text="Savings", font=("calibri", 40, "bold"), fg="black")
title.grid(row=0, column=0, padx=50, pady=30, columnspan=2)

#First code

def main():
    # Input savings goal and current savings from the user
    try:
        savings_goal = float(input("Enter the savings goal: "))
        current_savings = float(input("Enter the current savings: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values.(Note the input should have a decimal place)")
        return

    # Input probability from the user
    try:
        confidence = float(input('Enter a number between 0 and 1 based on how much confidence you have in this investment: '))
        historical_performance = float(input('Enter a number between 0 and 1 based on historical performance of this investment: '))
        risk_tolerance = float(input('Enter a number between 0 and 1, which represents how much risk you are ready to take: '))

        probability = calculate_probability(confidence, historical_performance, risk_tolerance)

        if 0 <= probability <= 1:
            weighted_return = calculate_weighted_return(probability, savings_goal, current_savings)
            print(f"Weighted return: {weighted_return}")
        else:
            print("Invalid probability. Please enter a value between 0 and 1.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()



def calculate_probability(confidence, historical_performance, risk_tolerance):
    # Normalize inputs to ensure they are between 0 and 1
    confidence = max(0, min(1, confidence))
    historical_performance = max(0, min(1, historical_performance))
    risk_tolerance = max(0, min(1, risk_tolerance))

    # Weight factors (adjust as needed)
    confidence_weight = 0.4
    historical_performance_weight = 0.3
    risk_tolerance_weight = 0.3

    # Combine factors to calculate probability
    probability = (
        confidence_weight * confidence +
        historical_performance_weight * historical_performance +
        risk_tolerance_weight * risk_tolerance
    )

    # Normalize the final probability
    probability = max(0, min(1, probability))

    return probability

def prospect_utility(value, alpha=0.8, beta=2, lambda_=1, gamma=0.5):
    if value >= 0:
        return value**alpha
    else:
        return -lambda_ * (-value)**beta

def prospect_decision(probability, outcome, gamma=0.5):
    weighted_outcome = prospect_utility(outcome) * probability**gamma
    return weighted_outcome

def calculate_weighted_return(probability, savings_goal, current_savings, gamma=0.5):
    outcome = savings_goal - current_savings
    weighted_return = prospect_decision(probability, outcome, gamma)
    return weighted_return

def main():
    savings_goal = 5000
    current_savings = 2000

    # Input probability from the user
    try:
        confidence = float(input('Enter a number between 0 and 1 based on how much confidence you have in this investment: '))
        historical_performance = float(input('Enter a number between 0 and 1 based on historical performance of this investment: '))
        risk_tolerance = float(input('Enter a number between 0 and 1, which represents how much risk you are ready to take: '))

        probability = calculate_probability(confidence, historical_performance, risk_tolerance)

        if 0 <= probability <= 1:
            weighted_return = calculate_weighted_return(probability, savings_goal, current_savings)
            print(f"Weighted return: {weighted_return}")
        else:
            print("Invalid probability. Please enter a value between 0 and 1.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

    #if weighted_return >= 0 and weighted_return <= 427.75:
     #   print('Its recomended you look for an alternate investement option as the weighted return is not providing a favourable outcome.')
    #elif weighted_return >= 427.76 and weighted_return <= 470:
     #   print('''Although the weighted return is not bad, Its recomended that you talk to you investment advisors before investing as, 
#the weighted return indicates that it might not be a favourable outcome.''')
#    else:
#        print('''The weighted return shows that you can go ahead with the investment. But it is always advised to consult with
#your fianncial advisor before making an investment. ''')
    
#if __name__ == "__main__":
#    main()



#Second code 


def calculate_probability(confidence, historical_performance, risk_tolerance):
    # Normalize inputs to ensure they are between 0 and 1
    confidence = max(0, min(1, confidence))
    historical_performance = max(0, min(1, historical_performance))
    risk_tolerance = max(0, min(1, risk_tolerance))

    # Weight factors (adjust as needed)
    confidence_weight = 0.4
    historical_performance_weight = 0.3
    risk_tolerance_weight = 0.3

    # Combine factors to calculate probability
    probability = (
        confidence_weight * confidence +
        historical_performance_weight * historical_performance +
        risk_tolerance_weight * risk_tolerance
    )

    # Normalize the final probability
    probability = max(0, min(1, probability))

    return probability

# alpha : When α is close to 1, the utility function exhibits a more linear shape for positive outcomes.
# The higher the αα, the more "concave" or curvature there is in the utility function for gains.

# Beta : The β parameter affects the shape of the utility function for negative outcomes (losses). It controls the curvature of the function 
#        for negative values.
#    A higher value of β makes the utility function more concave for negative outcomes.
#    The β parameter reflects the idea that people tend to be more sensitive to losses than to equivalent gains.

# Gamma :     The γ parameter is used in the probability weighting part of the function. It influences how 
#             much weight is given to the probability of an outcome.
#             A higher γ makes the probability weighting more "powerful" and can lead to more pronounced changes 
#             in the shape of the utility function based on perceived probabilities.
#             γ is often associated with the degree of risk aversion. Higher values of γγ indicate higher risk aversion.
def prospect_utility(value, alpha=0.8, beta=2, lambda_=1):
    if value >= 0:
        return value**alpha
    else:
        return -lambda_ * (-value)**beta

def prospect_decision(probability, outcome, gamma=0.5):
    weighted_outcome = prospect_utility(outcome) * probability**gamma
    return weighted_outcome

def calculate_weighted_return(probability, savings_goal, current_savings, gamma=0.5):
    outcome = savings_goal - current_savings
    weighted_return = prospect_decision(probability, outcome, gamma)
    return weighted_return

def convert_to_percentage(weighted_return,savings_goal):
    percentage_return = (weighted_return * 100)//savings_goal
    return percentage_return

def main():
    # Input savings goal and current savings from the user
    try:
        savings_goal = float(input("Enter the savings goal: "))
        current_savings = float(input("Enter the current savings: "))
        
    except ValueError:
        print("Invalid input. Please enter valid numeric values. (Note the input should have a decimal place)")
        return

    # Input probability from the user
    try:
        confidence = float(input('Enter a number between 0 and 1 based on how much confidence you have in this investment: '))
        historical_performance = float(input('Enter a number between 0 and 1 based on historical performance of this investment: '))
        risk_tolerance = float(input('Enter a number between 0 and 1, which represents how much risk you are ready to take: '))

        probability = calculate_probability(confidence, historical_performance, risk_tolerance)

        if 0 <= probability <= 1:
            weighted_return = calculate_weighted_return(probability, savings_goal, current_savings)
            print(f"Weighted return: {weighted_return}")

            # Convert to percentage and print
            percentage_return = convert_to_percentage(weighted_return,savings_goal)
            print(f"Percentage Return: {percentage_return}%")
        else:
            print("Invalid probability. Please enter a value between 0 and 1.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")

if __name__ == "__main__":
    main()



root.mainloop()
