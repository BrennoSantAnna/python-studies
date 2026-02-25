# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    value = get_integer("Enter the number: ")

    successor = value + 1
    predecessor = value - 1

    print(f"Analyzing the number {value}, "
          f"its successor is {successor} and "
          f"its predecessor is {predecessor}.")


if __name__ == "__main__":
    main()
