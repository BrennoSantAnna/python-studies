# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

GALLON_OF_PAINT = 2.0


def get_float(prompt: str) -> float:
      while True:
          try:
              return float(input(prompt))
          except ValueError:
              print("Please enter a valid number.")


def area_calculation(value1: float, value2: float) -> float:
    return value1 * value2


def paint_consumption_calculation(area: float) -> float:
    return area / GALLON_OF_PAINT


def main() -> None:
    width = get_float("Enter the width (m): ")
    height = get_float("Enter the height (m): ")

    area = area_calculation(width, height)
    paint_needed = paint_consumption_calculation(area)

    print(f"Your wall measures {width:.2f}x{height:.2f} meters "
          f"and has area of {area:.2f}m².\n"
          f"To paint this wall, you will need {paint_needed:.2f} liters of paint.")


if __name__ == "__main__":
    main()
