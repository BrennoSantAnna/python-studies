# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar
# R$ 7,00 por cada Km acima do limite

SPEED_LIMIT = 80


def get_car_velocity(prompt: str) -> float:
    while True:
        try:
            velocity = float(input(prompt))
            return velocity
        except ValueError:
            print("Please enter a valid number.")


def calculate_fine(velocity: float) -> float:
    if velocity > SPEED_LIMIT:
        return (velocity - SPEED_LIMIT) * 7.0
    return 0.0


def show_result(velocity: float) -> float:
    fine = calculate_fine(velocity)

    if fine > 0:
        print(f"\033[31mFINE! You exceeded the speed limit of {SPEED_LIMIT}km/h.\n"
              f"You must pay a fine of US$ {fine:.2f}!\033[m\n")

        print(f"\033[32mHave a nice day! Drive safely\033[m")


def main() -> None:
    velocity = get_car_velocity("What is the car's current speed? ")
    show_result(velocity)


if __name__ == "__main__":
    main()