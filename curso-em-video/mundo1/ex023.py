# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# 1834 - unidade: 4, dezena: 3, centena: 8, milhar: 1


def get_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))

            if value < 0 or value > 9999:
                print("Please enter a number between 0 and 9999.")
                continue

            return value

        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    value = get_integer("Enter a integer number: ")

    print(f"Analyzing the number: {value}:\n"
          f"Unit: {value // 1 % 10}\n"
          f"Ten: {value // 10 % 10}\n"
          f"Hundred: {value // 100 % 10}\n"
          f"Thousand: {value // 1000 % 10}")


if __name__ == "__main__":
    main()
