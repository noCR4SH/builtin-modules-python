"""
Example using csv, os, and datetime: Expense Tracker
This script uses the csv, os, and datetime modules to implement a simple expense tracker. 
It allows the user to add expenses, which are then saved to a CSV file with a timestamp.
"""

import csv
import os
from datetime import datetime

def add_expense(amount, category):
    filename = "expenses.csv"
    # Check if the file exists to write headers
    file_exists = os.path.isfile(filename)
    with open(filename, "a", newline='') as csvfile:
        fieldnames = ['Date', 'Amount', 'Category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader() # Write header only once

        now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        writer.writerow({'Date': now, 'Amount': amount, 'Category': category})

    print(f"Added expense {amount} in category '{category}' on {now}")


while True:
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        add_expense(amount, category)
    elif choice == '2':
        print("Exiting the program")
        break
    else:
        print("Invalid choice. Please try again.")
