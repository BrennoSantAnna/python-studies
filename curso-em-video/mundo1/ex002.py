# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.


def is_valid_name(name: str) -> bool:
    return all(word.isalpha() for word in name.split())


def get_name() -> str:
    while True:
        name = input("Enter your name: ").strip()

        if not name:
            print("The name cannot be empty.")
            continue

        if not is_valid_name(name):
            print("Enter a valid name.")
            continue

        return name


def main():
    name = get_name()
    print(f"Nice to meet you, {name}!")


if __name__ == "__main__":
    main()
