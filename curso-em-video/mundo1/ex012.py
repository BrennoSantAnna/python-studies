# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

DISCOUNT = 0.05


def get_price(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_discount(amount: float) -> float:
    return amount * DISCOUNT


def main() -> None:
    original_price = get_price("Enter the price: US$ ")
    new_price = original_price - calculate_discount(original_price)

    print(f"The original product that cost US$ {original_price:.2f}, "
          f"will now cost US$ {new_price:.2f} with 5% discount.")


if __name__ == "__main__":
    main()