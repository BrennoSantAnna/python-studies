# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"


def get_city_name(prompt: str) -> str:
    while True:
        city = input(prompt).strip()

        if not city:
            print("City cannot be empty.")
            continue

        if not city.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return city


def main() -> None:
    city = get_city_name("Enter a city name: ")

    print(city.upper().startswith("SANTO"))


if __name__ == "__main__":
    main()