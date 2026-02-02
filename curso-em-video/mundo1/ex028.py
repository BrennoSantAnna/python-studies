# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá 
# escrever na tela se o usuário venceu ou perdeu

# Importação de módulos necessários para o funcionamento do programa
from time import sleep
from random import randint

print("\033[0;33m-=-\033[m" * 20)
print("\033[0;34mVou pensar em um número entre 0 e 5. Tente advinhar...\033[m")
print("\033[0;33m-=-\033[m" * 20)

numero_computador = randint(0, 5)
numero_jogador = int(input("Em que número eu pensei? "))

sleep(0.5)
print("\033[0;35mPROCESSANDO...\033[m")
sleep(3)

if numero_computador == numero_jogador:
    print(f"\033[0;32;1mPARABÉNS! Você conseguiu me vencer!\033[m")
else:
    print(f"\033[0;31;1mGANHEI! Eu pensei no número {numero_computador} e não no {numero_jogador}!\033[m")