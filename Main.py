import tkinter as tk
from tkinter import ttk

def create_exp_dictionary():
    exp_type = exp_entry1.get()
    exp_amount = exp_entry2.get()
    essential = checkbox_var1.get()
    non_essential = checkbox_var2.get()

    exp_data = {
        "Type": exp_type,
        "Amount": exp_amount,
        "Essential": essential,
        "Non-Essential": non_essential
    }

    tree_exp.insert("", tk.END, values=(exp_data["Type"], exp_data["Amount"], exp_data["Essential"], exp_data["Non-Essential"]))

    exp_entry1.delete(0, tk.END)
    exp_entry2.delete(0, tk.END)
    checkbox_var1.set(False)
    checkbox_var2.set(False)


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

root = tk.Tk()
root.title("Expense Tracker")
root.configure(bg = "black")
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

notebook.add(tab1, text="Expenses")
notebook.add(tab2, text="Income")
notebook.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

title = tk.Label(tab1, text="Expense Tracker", font=("Georgia", 60, "bold"), fg = "blue")
title.grid(row=0, column=0, padx=50, pady=30, columnspan=2)

exp_label = tk.Label(tab1, text="Expenses", font=("Georgia", 20, "bold"), fg = "red")
exp_label.grid(row=1, column=0, padx=10, pady=15, columnspan=2)

exp_entry_label1 = tk.Label(tab1, text="Expense Type:")
exp_entry_label1.grid(row=2, column=0, padx= 10, pady=5)
exp_entry1 = tk.Entry(tab1, width=25)
exp_entry1.grid(row=2, column=1, padx=10, pady=5)

exp_entry_label2 = tk.Label(tab1, text="Expense Amount:")
exp_entry_label2.grid(row=3, column=0, padx=10, pady=5)
exp_entry2 = tk.Entry(tab1, width=25)
exp_entry2.grid(row=3, column=1, padx=10, pady=5)

exp_checkbox_label = tk.Label(tab1, text="Expense Category:")
exp_checkbox_label.grid(row=4, column=0, padx=10, pady=5)

checkbox_var1 = tk.BooleanVar()
checkbox1 = tk.Checkbutton(tab1, text="Essential", variable=checkbox_var1)
checkbox1.grid(row=4, column=1, sticky="w")

checkbox_var2 = tk.BooleanVar()
checkbox2 = tk.Checkbutton(tab1, text="Non-Essential", variable=checkbox_var2)
checkbox2.grid(row=4, column=1, sticky="e")

exp_submit_button = tk.Button(tab1, text="Submit", command=create_exp_dictionary, fg = "white", bg = "black")
exp_submit_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

inc_label = tk.Label(tab2, text="Income", font=("Georgia", 15, "bold"), fg = "red")
inc_label.grid(row=1, column=0, padx=10, pady=15, columnspan=2)

inc_entry_label1 = tk.Label(tab2, text="Income Type:")
inc_entry_label1.grid(row=2, column=0, padx=10, pady=5)
inc_entry1 = tk.Entry(tab2, width=25)
inc_entry1.grid(row=2, column=1, padx=10, pady=5)

inc_entry_label2 = tk.Label(tab2, text="Income Amount:")
inc_entry_label2.grid(row=3, column=0, padx=10, pady=5)
inc_entry2 = tk.Entry(tab2, width=25)
inc_entry2.grid(row=3, column=1, padx=10, pady=5)

inc_submit_button = tk.Button(tab2, text="Submit", command=create_income_dictionary, fg = "white", bg = "black")
inc_submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
columns_exp = ("Type", "Amount", "Essential", "Non-Essential")
tree_exp = ttk.Treeview(tab1, columns=columns_exp, show="headings")

for col in columns_exp:
    tree_exp.heading(col, text=col)
    tree_exp.column(col, anchor="center")

tree_exp.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
columns_inc = ("Type", "Amount")
tree_inc = ttk.Treeview(tab2, columns=columns_inc, show="headings")

for col in columns_inc:
    tree_inc.heading(col, text=col)
    tree_inc.column(col, anchor="center")

tree_inc.grid(row=6, column=0, columnspan=3, padx=10, pady=10)
delete_exp_button = tk.Button(tab1, text="Delete Selected", command=delete_expense_item, fg = "white", bg = "black")
delete_exp_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)
delete_inc_button = tk.Button(tab2, text="Delete Selected", command=delete_income_item, fg = "white", bg = "black")
delete_inc_button.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()