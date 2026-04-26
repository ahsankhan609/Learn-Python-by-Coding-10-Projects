def calculate_expense_split(total_expense: int, number_of_people: int, currency: str = "USD") -> None:
    """
    this function will take 3 arguments:
    total expense amount:
    number of people in which expense will be split
    currency pair - default is "USD"

    this program then calculate split of each person in the defined currency.

    Example:
        calculate_expense_split(10000, 5, "eur")
    """

    if number_of_people < 1:
        raise ValueError("number_of_people must be greater than one(1)")

    share_of_person: float = total_expense / number_of_people
    percentage_of_person: float = share_of_person / total_expense
    print(f"Total per head expense will be: {share_of_person:,.2f} {currency}")
    print(f"Total expense Share % will be: {percentage_of_person:,.2%} {currency}")
    # here 2 means 2 decimal places after answer
    # here f means answer should be in flot
    # here % means answer should be in percentage
    # to show results in scientific notation we use e
    # to put , in 000 use , after :
    # to make some space in our results, we give a width number after : like :15,.2f
    # it will give 15 width and , separate and 2 flot numbers after result


if __name__ == "__main__":
    calculate_expense_split(50000, 15, "eur")
