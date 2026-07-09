expenses = []
def add_expense():
    amt = float(input("Enter the expense amount: "))
    des = input("Enter the expense description: ")
    cat = input("Enter the expense category: ")
    expenses.append({'amount': amt, 'description': des, 'category': cat})

def view_expense():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Viewing all expenses...")
        print("Amount\tDescription\tCategory")
        for expense in expenses:
            print(f"{expense['amount']}\t{expense['description']}\t{expense['category']}")

def total_spent():
    if not expenses:
        print("No expenses recorded.")
    else:
        print("Calculating total spent...")
        total = 0
        for i in range(len(expenses)):
            total += expenses[i]['amount']
        print(f"Total amount spent: ${total:.2f}")


while True:
    print("======-- Expense Tracker Menu --======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spent")
    print("4. Exit")

    choice = input("enter your choice freom above menu:")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        total_spent()
    elif choice == '4':
        print("thank you for using the expense tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

