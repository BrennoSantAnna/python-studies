# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

INCREASE = 0.15


def get_original_salary(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_increase(amount: float) -> float:
    return amount * INCREASE


def calculate_new_salary(amount: float) -> float:
    return amount * (1 + INCREASE)


def main() -> None:
    original_salary = get_original_salary("Enter the salary: US$ ")
    new_salary = calculate_new_salary(original_salary)

    print(f"An employee who was earning US$ {original_salary:.2f} will receive, "
          f"US$ {new_salary:.2f}, a 15% increase.")


if __name__ == "__main__":
    main()
