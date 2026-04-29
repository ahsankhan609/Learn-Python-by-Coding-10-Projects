import json


def load_rates(json_file: str) -> dict[str, dict[str, str | float]]:
    with open(json_file, 'r') as file:
        return json.load(file)


def convert(amount: float, base: str, to: str, rates: dict[str, dict[str, str | float]]) -> float:
    base: str = base.lower()
    to: str = to.lower()

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    if from_rates is not None and to_rates is not None:
        if base == 'eur':  # this json file use EUR as base currency , that's why we use it here
            return amount * to_rates['rate']
        else:
            return amount * (to_rates['rate'] / from_rates['rate'])
    else:
        print("Please enter valid currency name.")
        return 0.0


def main() -> None:
    amount_to_convert: int = abs(int(input('Enter amount to convert: ')))
    from_currency: str = str(input('Enter currency name from convert: '))
    to_currency: str = str(input('Enter currency name to convert: '))

    rates: dict[str, dict] = load_rates('rates.json')
    result: float = convert(amount=amount_to_convert, base=from_currency, to=to_currency, rates=rates)
    print(f'you convert {amount_to_convert}, {from_currency} to {result:,.4f} {to_currency}')


if __name__ == '__main__':
    main()

"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user enters a rate that doesn't
   exist, the program tells them that the currency is invalid, then show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro.
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API.
4. This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script.
"""
