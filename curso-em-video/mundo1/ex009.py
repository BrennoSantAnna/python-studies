# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def calculate_multiplication(number: int) -> str:
    result = ""
    for cont in range(1, 11):
        result += f"{number} x {cont} = {number * cont}\n"
    return result


def main() -> None:
    value = get_integer("Enter a integer number: ")

    print(f"\nThe multiplication table for the number {value} is:")
    print(calculate_multiplication(value))


if __name__ == "__main__":
    main()
