# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
# para viagens de até 200Km e R$ 0,45 para viagens mais longas


def get_kilometer(prompt: str) -> float:
    while True:
        try:
            distance = float(input(prompt))
            return distance
        except ValueError:
            print("Please enter numbers only.")


def calculate_price(distance: float) -> float:
    if distance <= 200:
        price = 0.50
    else:
        price = 0.45

    return distance * price


def main() -> None:
    distance = get_kilometer("How far is your trip? ")

    print(f"You are about to embark on a {distance:.2f} kilometer trip.\n"
          f"And your fare will be US$ {calculate_price(distance):.2f}")


if __name__ == "__main__":
    main()