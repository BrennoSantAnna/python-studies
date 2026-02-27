# Crie um prograrma que leia uma quantia de dinheiro que uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar. Considere U$ 1.00 = R$ 3.27

EXCHANGE_RATE = 5.14


def get_amount(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid amount.")


def dollar_conversion_calculation(value: float) -> float:
    return value / EXCHANGE_RATE


def main() -> None:
    brazilian_currency = get_amount("Enter a Brazilian value: R$ ")

    print(f"With R$ {brazilian_currency:.2f}, "
          f"you can buy US$ {dollar_conversion_calculation(brazilian_currency):.2f}")


if __name__ == "__main__":
    main()
