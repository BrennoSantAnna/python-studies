# Desenvolva um programa que leia o comprimento
# de três retas e diga ao usuário se elas podem
# ou não formar um triângulo


def menu() -> None:
    print("-=" * 13)
    print("Triangle Analyzer")
    print("-=" * 13)


def get_segments(prompt1: str, prompt2: str, prompt3: str) -> tuple[int, int, int]:
    while True:
        try:
            a = float(input(prompt1))
            b = float(input(prompt2))
            c = float(input(prompt3))

            return a, b, c

        except ValueError:
            print("Please enter valid integers.")


def is_triangle(a: int, b: int, c: int) -> None:
    return a < b + c and b < a + c and c < a + b


def main() -> None:
    menu()

    a, b, c = get_segments(
        "First value: ",
        "Second value: ",
        "Third value: "
    )

    if is_triangle(a, b, c):
        print("The segments above may form a triangle!")
    else:
        print("The segments above cannot form a triangle!")


if __name__ == "__main__":
    main()