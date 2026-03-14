# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente
# Ex. Ana Maria de Souza - primeiro = Ana - último = Souza


def get_full_name(prompt: str) -> str:
    while True:
        full_name = input(prompt).strip()

        if not full_name:
            print("Name cannot be empty.")
            continue

        if not full_name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return full_name


def split_name(prompt: str) -> tuple[str, str]:
    separate = prompt.split()
    first = separate[0]
    last = separate[-1]

    return separate, first, last


def main() -> None:
    full_name = get_full_name("Enter your full name: ")

    separate, first, last = split_name(full_name)

    print(f"Nice to meet you!\n"
          f"Your first name is {first}.\n"
          f"Your last name is {last}.")

if __name__ == "__main__":
    main()