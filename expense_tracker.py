import json 
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read saved expenses. Starting with an empty list.")
            return []


def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        amount = float(input("Enter amount (₹): "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
        category = input("Enter category(Food/Travel/Shopping/etc.): ").strip()
        description = input("Enter description: ").strip()

        if not category:
            category = "Other"

        expense = {
            "amount": amount,
            "Category": category.title(),
            "description": description or "No description"
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("NO expenses recorded yet.")
        return

    print("\n --- All expenses ---")
    for number, expenses in enumerate(expenses, start = 1):
        print(
    f"{number}. ₹{expense['amount']:.2f} | "
    f"{expense['category']} | "
    f"{expense['description']}"
)

def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spending: ₹{total:.2f}")

def category_summary(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}

    for expense in expenses:
        category = expense["category"]
    totals[category] = totals.get(category, 0) + expense["amount"]

    print("\n--- Category-wise spending ---")
    for category, amount in sorted(totals.items()):
        print(f"{category}: ₹{amount:.2f}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== PERSONAL EXPENSE TRACKER ===")
        print("1. Add Expense")
        print("2. View spending")
        print("3. Total Spending")
        print("4. Category-wise spending")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            category_summary(expenses)
        elif choice == "5":
            print("Thanks for using the expense Trackers. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5")

    print("Python file started!")

if __name__ == "__main__":
    print("Starting main function...")
    main()

