def calculate_net_pay(monthly_income: float, tax_rate: float, expenses: dict, currency: str = "USD") -> None:
    """
    Calculate and display the monthly and yearly net pay after tax and expenses.
    """
    yearly_income: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    
    monthly_net_pay: float = monthly_income - monthly_tax
    yearly_net_pay: float = yearly_income - yearly_tax
    
    total_expenses = sum(expenses.values())
    remaining_balance = monthly_net_pay - total_expenses
    
    print(f"\nMonthly Income: {monthly_income:,.2f} {currency}")
    print(f"Monthly Net Pay after Tax: {monthly_net_pay:,.2f} {currency}")
    print(f"Total Expenses: {total_expenses:,.2f} {currency}")
    print(f"Remaining Balance: {remaining_balance:,.2f} {currency}")
    print(f"Yearly Income: {yearly_income:,.2f} {currency}")
    print(f"Yearly Net Pay after Tax: {yearly_net_pay:,.2f} {currency}")

def get_float_input(prompt: str) -> float:
    """Safely gets a float input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_expenses() -> dict:
    """Collects expenses from the user and returns them as a dictionary."""
    expenses = {}
    while True:
        expense_name = input("Enter an expense name (or type 'done' to finish): ")
        if expense_name.lower() == 'done':
            break
        amount = get_float_input(f"Enter amount for {expense_name}: ")
        expenses[expense_name] = amount
    return expenses

def main() -> None:
    monthly_income = get_float_input("Enter your monthly income: ")
    tax_rate = get_float_input("Enter your tax rate (%): ")
    expenses = get_expenses()
    calculate_net_pay(monthly_income, tax_rate, expenses, currency="USD")

if __name__ == "__main__":
    main()
