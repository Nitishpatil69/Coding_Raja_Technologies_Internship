import json
from datetime import datetime

# Initialize an empty list to store transactions.
transactions = []

# Function to input expenses and income.
def record_transaction():
    print("\nRecord a Transaction")
    print("-" * 20)
    category = input("Category (Expense/Income): ")
    amount = float(input("Amount (INR): "))
    
    while True:
        date = input("Date (YYYY-MM-DD): ")
        if is_valid_date(date):
            transaction = {"category": category, "amount": amount, "date": date}
            transactions.append(transaction)
            print("Transaction recorded successfully.")
            break
        else:
            print("Invalid date format. Please use YYYY-MM-DD format.")

# Function to calculate remaining budget.
def calculate_budget():
    total_income = sum(transaction["amount"] for transaction in transactions if transaction["category"] == "Income")
    total_expenses = sum(transaction["amount"] for transaction in transactions if transaction["category"] == "Expense")
    remaining_budget = total_income - total_expenses
    return remaining_budget

# Function to check if a date is valid.
def is_valid_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Function to save transactions to a JSON file.
def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)
        print("Transactions saved to 'transactions.json'.")

# Main program loop
while True:
    print("\nPersonal Budget Tracker")
    print("-" * 30)
    print("Options:")
    print("1. Record a transaction")
    print("2. Calculate budget")
    print("3. Save transactions")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        record_transaction()
    elif choice == "2":
        remaining_budget = calculate_budget()
        print(f"Remaining budget: ₹{remaining_budget:.2f}")
    elif choice == "3":
        save_transactions()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
