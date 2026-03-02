# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

# Importing modules necessary for the program to run
import math


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_trigonometric_functions(angle: float) -> tuple[float, float, float]:
    radians = math.radians(angle)
    return {
        math.sin(radians),
        math.cos(radians),
        math.tan(radians),
    }


def main() -> None:
    angle = get_float("Enter the angle: ")

    sine, cosine, tangent = calculate_trigonometric_functions(angle)

    print(f"The angle of {angle} has "
          f"a sine of {sine:.2f}, "
          f"a cosine of {cosine:.2f} and "
          f"a tangent of {tangent:.2f}.")


if __name__ == "__main__":
    main()
