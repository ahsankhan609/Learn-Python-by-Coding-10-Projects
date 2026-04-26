from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation, getcontext
from typing import Union

# Set a sensible precision for money calculations
getcontext().prec = 28

Money = Union[int, float, Decimal]


@dataclass(frozen=True)
class ExpenseSplit:
    total: Decimal
    number_of_people: int
    share_per_person: Decimal
    share_percentage: Decimal  # percent 0..100
    currency: str


def calculate_expense_split(total_expense: Money, number_of_people: int, currency: str = "USD") -> ExpenseSplit:
    """
    Calculate how a monetary expense is split among people.

    Args:
        total_expense: Total expense amount (int, float, or Decimal). Must be > 0.
        number_of_people: Number of people to split the expense. Must be >= 1.
        currency: Currency code (3-letter string). Defaults to "USD".

    Returns:
        ExpenseSplit dataclass containing computed values.

    Raises:
        ValueError: If inputs are invalid.
    """
    if number_of_people < 1:
        raise ValueError("number_of_people must be at least 1")
    try:
        total = Decimal(total_expense)
    except (InvalidOperation, TypeError):
        raise ValueError("total_expense must be a numeric value")

    if total <= 0:
        raise ValueError("total_expense must be greater than 0")

    if not isinstance(currency, str) or not currency:
        raise ValueError("currency must be a non-empty string")

    # Compute using Decimal, round share to 2 decimal places (standard money rounding)
    share = (total / Decimal(number_of_people)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    # Compute percentage (0..100) with 2 decimal places
    percentage = ((share / total) * Decimal(100)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return ExpenseSplit(
        total=total,
        number_of_people=number_of_people,
        share_per_person=share,
        share_percentage=percentage,
        currency=currency.upper(),
    )


def format_expense_split(es: ExpenseSplit) -> str:
    """
    Return a human-readable formatted string for an ExpenseSplit.
    """
    total_str = f"{es.total:,.2f}"
    share_str = f"{es.share_per_person:,.2f}"
    pct_str = f"{es.share_percentage:,.2f}%"
    return (
        f"If {es.number_of_people} people go on a trip and spend {total_str} {es.currency} in total:\n"
        f"- Each person pays: {share_str} {es.currency}\n"
        f"- Share of total: {pct_str} (per person)"
    )


if __name__ == "__main__":
    try:
        result = calculate_expense_split(15000, 3, "gbp")
        print(format_expense_split(result))
    except Exception as e:
        print(f"Error: {e}")
