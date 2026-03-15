# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu

# Importing the modules required for the program to run
from time import sleep
from random import randint


def computer_random_number() -> int:
    return randint(0, 5)


def player_number(prompt: str) -> int:
    while True:
        try:
            number = int(input(prompt))

            if 0 <= number <= 5:
                return number

            print("Number must be between 0 and 5.")

        except ValueError:
            print("Please enter a valid integer between 0 and 5.")


def menu() -> None:
    print("\033[0;33m-=-\033[m" * 20)
    print("\033[0;34mI'm going to think of a number between 0 and 5. Try to guess it...\033[m")
    print("\033[0;33m-=-\033[m" * 20)


def winner(computer: int, player: int) -> None:
    if computer == player:
        print(f"\033[0;32;1mCONGRATULATIONS! You managed to beat me!\033[m")
    else:
        print(f"\033[0;31;1mI WON! I thought of the number {computer}, not {player}!\033[m")


def main() -> None:
    menu()

    computer = computer_random_number()
    player = player_number("Your guess [0 - 5]: ")


    sleep(0.5)
    print("\033[0;35mPROCESSING...\033[m")
    sleep(3)

    winner(computer, player)


if __name__ == "__main__":
    main()