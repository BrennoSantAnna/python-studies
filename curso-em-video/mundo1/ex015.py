# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0.15 por km rodado

DAILY_CAR_RENTAL_COST = 60
COST_PER_KILOMETER_TRAVELED = 0.15


def get_days(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_kilometer_traveled(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_total_rental_cost(days: int, kilometer: float) -> float:
    return (days * DAILY_CAR_RENTAL_COST) + (kilometer * COST_PER_KILOMETER_TRAVALED)


def main() -> None:
    rented_days = get_days("Enter the total number of days rented: ")
    kilometers_traveled = get_kilometer_traveled("Enter the total number of kilometers traveled: ")

    print(f"The total value to pay is US$ {total_value_calculation(rented_days, kilometers_traveled):.2f}")


if __name__ == "__main__":
    main()
