# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(prompt: float) -> str:
    return (
        f"{prompt / 1000}km\n"
        f"{prompt / 100}hm\n"
        f"{prompt / 10}dam\n"
        f"{prompt * 10}dm\n"
        f"{prompt * 100}cm\n"
        f"{prompt * 1000}mm\n"
    )


def main() -> None:
    value = get_float("Enter a value (m): ")

    print(f"\nThe measurement of {value} meters correspondts to:")
    print(calculate(value))


if __name__ == "__main__":
    main()
