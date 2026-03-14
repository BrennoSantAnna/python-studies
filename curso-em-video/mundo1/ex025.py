# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome


def get_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return name


def main() -> None:
    name = get_name("Enter your name: ")

    has_silva = "SILVA" in name.upper()

    print(f"Does the name contain 'Silva'? {has_silva}")


if __name__ == "__main__":
    main()