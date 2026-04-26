def calculate_expense_split(total_expense: int, number_of_people: int, currency: str = "USD") -> None:
    """
    Description:
    this program calculate split for each person, from total expense of vacation, in the defined currency as multiple strings.

    this function will take 3 arguments:

    Parameters:
    - total expense amount (float):
    - number of people in which expense will be split (int):
    - currency pair - default is "USD" (str):

    Raises:
        ValueError - if total expense amount is not a positive integer.
        ValueError - number of people must be greater than one(1).
    Example:
        calculate_expense_split(10000, 5, "eur")

    Returns:
        if 15 people goes on a trip, and spend 50,000 in total.
        your expense will be: 3,333.33 EUR per person.
        and your expense share % in total expense of 50,000 will be: 6.67%, i.e 3,333.33 EUR per person.
    """

    if number_of_people < 1:
        raise ValueError("number_of_people must be greater than one(1)")
    elif total_expense <= 0:
        raise ZeroDivisionError(f"you entered {total_expense} expense, expenses must be greater than zero")

    share_of_person: float = total_expense / number_of_people
    percentage_of_person: float = share_of_person / total_expense
    print(f"if {number_of_people} people goes on a trip, and spend {total_expense:,} {currency.upper()} in total.")
    print(f"your expense will be: {share_of_person:,.2f} {currency.upper()} per person.")
    print(
        f"and your expense share % in total expense of {total_expense:,} will be: {percentage_of_person:,.2%}, i.e {share_of_person:,.2f} {currency.upper()} per person.")
    # here 2 means 2 decimal places after answer
    # here f means answer should be in flot
    # here % means answer should be in percentage
    # to show results in scientific notation we use e
    # to put , in 000 use , after :
    # to make some space in our results, we give a width number after : like :15,.2f
    # it will give 15 width and , separate and 2 flot numbers after result


if __name__ == "__main__":
    try:
        calculate_expense_split(15000, 3, "gbp")
    except Exception as e:
        print(e)
