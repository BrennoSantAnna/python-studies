# Crie um programa que leia dois números e mostre a soma entre eles.


def get_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    first_value = get_integer("Enter the first number: ")
    second_value = get_integer("Enter the second number: ")

    result = first_value + second_value

    print(f"The sum between {first_value} and {second_value} is {result}")


if __name__ == "__main__":
    main()
