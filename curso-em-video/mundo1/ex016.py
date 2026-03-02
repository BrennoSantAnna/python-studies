# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.
# Ex.: 6.127 - O número 6.127 tem a parte inteira 6


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_integer_part(value: float) -> int:
    return int(value)


def main() -> None:
    real_number = get_float("Enter a float number: ")
    integer_number = get_integer_part(real_number)

    print(f"The number entered was {real_number} "
          f"and your entire portion is {integer_number}")


if __name__ == "__main__":
    main()
