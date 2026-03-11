# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas e minúsculas
# 2. Quantas letras ao todo (sem considerar espaços)
# 3. Quantas letras tem o primeiro nome


def get_valid_name() -> str:
    while True:
        name = input("Enter your full name: ").strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return name


def get_first_name(name: str) -> str:
    return name.split()[0]


def count_letters_without_spaces(name: str) -> int:
    return len(name.replace(" ", ""))


def main() -> None:
    name = get_valid_name()
    first_name = get_first_name(name)

    print(f"Analyzing your name...\n"
          f"Your name in uppercase is: {name.upper()}\n"
          f"Your name in lowercase is: {name.lower()}\n"
          f"Total letters (without spaces): {count_letters_without_spaces(name)}\n"
          f"Your first name is {first_name(name)} and it has {len(first_name)} letters.")


if __name__ == "__main__":
    main()