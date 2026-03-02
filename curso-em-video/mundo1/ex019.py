# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

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

    chosen_student = random.choice(students)

    print(f"The chosen student is {chosen_student}")


if __name__ == "__main__":
    main()
