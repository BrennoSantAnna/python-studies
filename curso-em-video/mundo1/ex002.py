# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.


def get_valid_name() -> str:
    while True:
        name = input("Enter your name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return name


def main() -> None:
    name = get_valid_name()
    print(f"Welcome, {name}!")


if __name__ == "__main__":
    main()
