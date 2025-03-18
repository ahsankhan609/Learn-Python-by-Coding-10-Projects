# it should take out montly income and tax rate, and then calculate the monthly net take home pay

def calculate_net_pay(monthly_income: float, tax_rate: float, currency: str = "USD") -> None: 
    #if we use -> None: in the end of the function it means we are expecting None to rerurn from the function
    # if we use -> float: in the end of the function it means we are expecting a float to return from the function

    # now we will create local variables
    yearly_income: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12

    monthly_net_pay: float = monthly_income - monthly_tax
    yearly_net_pay: float = yearly_income - yearly_tax

    print(f"Monthly Income: {monthly_income:,.2f} {currency} and Monthly net pay: {monthly_net_pay:,.2f} {currency}")
    print(f"Yearly Income: {yearly_income:,.2f} {currency} and Yearly net pay: {yearly_net_pay:,.2f} {currency}")


# we can call the function with different arguments
calculate_net_pay(100, 20)
#calculate_net_pay(100, 20, "EUR")