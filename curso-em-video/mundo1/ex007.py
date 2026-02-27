# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_average(note1: float, note2: float) -> float:
    return (note1 + note2) / 2.0


def main() -> None:
    first_note = get_float("First note: ")
    second_note = get_float("Second note: ")

    average = get_average(first_note, second_note)

    print(f"The average between {first_note} and "
          f"{second_note} is {average}")


if __name__ == "__main__":
    main()