# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%


def get_salary(prompt: str) -> float:
    while True:
        try:
            salary = float(input(prompt))
            return salary
        except ValueError:
            print("Please enter a valid float.")


def calculate_increase(salary: float) -> float:
    if salary <= 1250.00:
        increase = 0.15
    else:
        increase = 0.1

    return (salary * increase) + salary


def main() -> None:
    salary = get_salary(f"What is the employee's salary? US$ ")
    new_salary = calculate_increase(salary)

    print(f"The employee used to earn US$ {salary:.2f}\n"
          f"With the increase, the new salary is US$ {new_salary:.2f}")

if __name__ == "__main__":
    main()