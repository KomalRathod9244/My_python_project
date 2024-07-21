'''Simple Personal Budget Tracker
Description: A program to help users track their income and expenses, providing a summary of their financial status.'''

class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append((amount, description, 'income'))
        print(f"Income of ${amount} added. New balance: ${self.balance}")

    def add_expense(self, amount, description):
           self.balance -= amount
           self.transactions.append((amount, description, 'expense'))
           print(f"Expense of ${amount} added. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current Balance: ${self.balance}")

    def view_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            amount, description, type = transaction
            print(f"{type.capitalize()}: ${amount} - {description}")

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Personal Budget Tracker ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
