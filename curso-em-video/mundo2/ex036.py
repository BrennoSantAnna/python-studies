# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt: str) -> float:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def calculating_monthly_payment(house_value: float, years: int) -> float:
    return house_value / (years * 12)


def calculate_payment_limit(salary: float) -> float:
    return salary * 0.3


def main() -> None:
    house_value = get_float(f"House value? $ ")
    salary = get_float(f"Buyer's salary? $ ")
    years = get_int(f"Years to pay: ")

    monthly_payment = calculating_monthly_payment(house_value, years)
    payment_limit = calculate_payment_limit(salary)

    print(f"To pay a house worth $ {house_value:.2f} in {years} years, "
          f"the monthly payment will be US$ {monthly_payment:.2f}")

    if monthly_payment <= payment_limit:
        print("Loan approved!")
    else:
        print("Loan denied!")


if __name__ == "__main__":
    main()