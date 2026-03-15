# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor


def get_integers(prompt1: str, prompt2: str, prompt3: str) -> tuple[int, int, int]:
    while True:
        try:
            a = int(input(prompt1))
            b = int(input(prompt2))
            c = int(input(prompt3))

            return a, b, c

        except ValueError:
            print("Please enter valid integers.")


def lowest_value(a: int, b: int, c: int) -> int:
    lowest = a

    if b < a and b < c:
        lowest = b
    if c < a and c < b:
        lowest = c

    return lowest


def highest_value(a: int, b: int, c: int) -> int:
    highest = a

    if b > a and b > c:
        highest = b
    if c > a and c > b:
        highest = c

    return highest


def main() -> None:
    a, b, c = get_integers(
        "First value: ",
        "Second value: ",
        "Third value: "
    )

    lowest = lowest_value(a, b, c)
    highest = highest_value(a, b, c)

    print(
        f"The lowest value entered was {lowest}\n"
        f"The highest value entered was {highest}"
    )

if __name__ == "__main__":
    main()