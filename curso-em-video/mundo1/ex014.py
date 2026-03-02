# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def convert_celsius_to_fahrenheit(value: float) -> float:
    return (value * 1.8) + 32


def main() -> None:
    temperature_in_degrees = get_float("Enter the temperature ºC: ")
    temperature_in_fahrenheit = convert_celsius_to_fahrenheit(temperature_in_degrees)

    print(f"The temperature of {temperature_in_degrees:.1f}ºC corresponds "
          f"to {temperature_in_fahrenheit:.1f}ºF.")


if __name__ == "__main__":
    main()
