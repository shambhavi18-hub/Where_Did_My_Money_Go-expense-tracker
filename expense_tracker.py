import json

expenses = []
def add_expense():
    amt = float(input("Enter the expense amount: "))
    des = input("Enter the expense description: ")
    cat = input("Enter the expense category: ")
    expenses.append({'amount': amt, 'description': des, 'category': cat})
    save_expenses()

def view_expense():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Viewing all expenses...")
        print("Amount\tDescription\tCategory")
        for i, expense in enumerate(expenses):
            print(f" {i }. {expense['amount']}\t{expense['description']}\t{expense['category']}")

def total_spent():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("calculating the amount..")
        total = 0
        for i in range(len(expenses)):
            total += expenses[i]['amount']
        
        print(f"Total amount spent: ${total:.2f}")
    
def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f, indent=4)

def load_expenses():
    global expenses
    try:
        with open('expenses.json', 'r') as f:
            expenses = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []
def delete_expense():
    if not expenses:
        print("No expenses recorded.")
    else:
        view_expense()
        index = int(input("Enter the index of the expense to delete: "))
        if 0 <= index < len(expenses):
            del expenses[index]
            save_expenses()
            print("Expense deleted successfully.")
        else:
            print("Invalid index. Please try again.")

load_expenses()

while True:
    print("======-- Expense Tracker Menu --======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("enter your choice freom above menu:")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        total_spent()
    elif choice == '4':
        delete_expense()
    elif choice == '5':
        save_expenses()
        print("thank you for using the expense tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

