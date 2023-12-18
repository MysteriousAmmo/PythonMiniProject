import csv
import tkinter as tk
from tkinter import ttk
import subprocess
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

exp_type_description_dict = {}
categories_dict = {}
categories = [] 
price_dict = {}



def categorize_items(item_dict):
    word_count_dict = {}
    item_category_dict = {}

    for item, description in item_dict.items():
        words = description.split()

        for word in words:
            if word in word_count_dict:
                word_count_dict[word] += 1
            else:
                word_count_dict[word] = 1

    for word, count in word_count_dict.items():
        if count >= 3: 
            category_name = word
            item_category_dict[category_name] = [item for item, desc in item_dict.items() if word in desc]

    return item_category_dict


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

    categories_dict = categorize_items(exp_type_description_dict)

    price_dict[exp_type] = exp_amount

    tree_exp.insert("", tk.END, values=(exp_data["Type"], exp_data["Amount"], exp_data["Description"], exp_data["Essential"]))

    exp_entry1.delete(0, tk.END)
    exp_entry2.delete(0, tk.END)
    exp_description_entry.delete(0, tk.END)
    checkbox_var1.set(False)


# def calculate_category_totals():
#     global category_totals
#     category_totals = {}

#     for category, items in categories_dict.items():
#         total_amount = sum(float(tree_exp.item(item, 'values')[1]) for item in items)
#         category_totals[category] = total_amount

#     print("Category Totals:", category_totals)


    # def exp_button():
    #     save_to_csv()
    #     create_exp_dictionary()
    #     calculate_category_totals()


#function to open anirudh's part
def openprospect(): 
    subprocess.run(["python", "C:\pythonproject\python_final_mini_project.py"])




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


#pulling amount and data in expected format for pie chart
amounttemp = 0
piechartdict = {}
def piechartdata(): 
    for category, items1 in categories_dict.items(): 
        for item, amount in price_dict.items(): 
            if item in items1: 
                amounttemp += amount
        piechartdict[category] = amounttemp

    return piechartdict


# test data - ouput should be correct
print(piechartdata)
    

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ...

def create_pie_chart():
    # Call the function to get the data for the pie chart
    piechart_data = piechartdata()

    # Extract labels and sizes from the dictionary
    labels = list(piechart_data.keys())
    sizes = list(piechart_data.values())

    # Colors for each category
    colors = ['#ff9999', '#66b3ff', '#99ff99']  # You can modify the colors as needed

    # Exploding the slices
    explode = tuple(0.1 for _ in labels)

    # Plotting the pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, explode=explode)
    ax.set_title('Expense Categories Pie Chart')

    # Create a Tkinter canvas to embed the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=tab3)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=4, column=0, columnspan=2, padx=10, pady=10)



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

#Open anirudh's part - opens a separate file
prospect_button = tk.Button(tab2, text="Open Prospect", command=openprospect, fg="white", bg="black")
prospect_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

title = tk.Label(tab3, text="Savings", font=("calibri", 40, "bold"), fg="black")
title.grid(row=0, column=0, padx=50, pady=30, columnspan=2)

pie_chart_button = tk.Button(tab3, text="Create Pie Chart", command=create_pie_chart, fg="white", bg="black")
pie_chart_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)



root.mainloop()
