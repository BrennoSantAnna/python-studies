# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Importing the math library to use the hypot function
import math


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_hypotenuse(opposite: float, adjacent: float) -> float:
    return math.hypot(opposite, adjacent)


def main() -> None:
    opposite_side = get_float("Enter the opposite side: ")
    adjacent_side = get_float("Enter the adjacent side: ")

    print(f"The hypotenuse will measure: {calculate_hypotenuse(opposite_side, adjacent_side):.2f}")


if __name__ == "__main__":
    main()
