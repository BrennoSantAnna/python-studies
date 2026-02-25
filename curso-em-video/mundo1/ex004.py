# Faça um programa que leia algo pelo teclado e mostre na tela o
# seu tipo primitivo e todas as informações possíveis sobre ele.


def main() -> None:
    value = input("Enter something: ")

    print(
        f"The primitive type of this value is {type(value)}\n"
        f"Contais only spaces? {value.isspace()}\n"
        f"Is numeric? {value.isnumeric()}\n"
        f"Is alphabetical? {value.isalpha()}\n"
        f"Is alphanumeric? {value.isalnum()}\n"
        f"Is it in uppercase? {value.isupper()}\n"
        f"Is it in lowercase? {value.islower()}\n"
        f"Is it capitalized? {value.istitle()}"
    )


if __name__ == "__main__":
    main()
