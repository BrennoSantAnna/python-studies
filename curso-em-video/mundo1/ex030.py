# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR


def get_integer(prompt: str) -> int:
    while True:
        try:
            number =  int(input(prompt))
            return number
        except ValueError:
            print("Please enter a valid integer.")


def check_even_odd(number: int) -> None:
    if number % 2 == 0:
        print(f"The number {number} is even")
    else:
        print(f"The number {number} is odd")


def main() -> None:
    number = get_integer("Enter a integer number: ")
    check_even_odd(number)


if __name__ == "__main__":
    main()