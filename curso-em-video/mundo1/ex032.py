# Faça um programa qaue leia um ano qualquer e mostre se ele é BISSEXTO

# Importing the modules required for the program to run
from datetime import date


def get_year(prompt: str) -> int:
    while True:
        try:
            year = int(input(prompt))
            return year
        except ValueError:
            print("Please enter a valid integer.")


def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def main() -> None:
    year = get_year(
        "Which year would you like to analyze? Enter 0 to analyze the current year: "
    )

    if year == 0:
        year = date.today().year

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")


if __name__ == "__main__":
    main()