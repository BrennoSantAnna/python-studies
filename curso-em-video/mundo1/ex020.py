# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# Importing modules necessary for the program to run
import random


def get_valid_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()

        if not name:
            print("Name cannot be empty.")
            continue

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        return name


def main() -> None:
    students = []

    for i in range(1, 5):
        name = get_valid_name(f"Enter the name of student {i}: ")
        students.append(name)

    random.shuffle(students)

    for position, student in enumerate(students, start=1):
        print(f"{position} - {student}")


if __name__ == "__main__":
    main()