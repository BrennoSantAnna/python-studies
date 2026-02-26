# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a raíz quadrada

from math import sqrt


def get_number(prompt: str) -> int | float:
	while True:
		value = input(prompt).strip()

		try:
			return int(value)
		except ValueError:
			try:
				return float(value)
			except ValueError:
				print("Please enter a valid integer or float.")


def main() -> None:
	number = get_number("Enter a number: ")

	if number < 0:
		print("Square root is not defined for negative numbers.")
		return

	double = number * 2
	triple = number * 3
	square_root = sqrt(number)

	print(f"Twice {number} is {double},\n"
	      f"Three times {number} is {triple},\n"
	      f"The square root of {number} is {square_root:.2f}.")


if __name__ == "__main__":
	main()
