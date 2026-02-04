# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o 
# total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

vitorias_jogador = 0

while True:
    jogador = int(input("Diga um valor: "))
    escolha_jogador = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    computador = randint(0, 10)

    escolha_computador = ""
    resultado = ""

    if escolha_jogador == "P":
        escolha_computador = "I"
    elif escolha_jogador == "I":
        escolha_computador = "P"

    soma = jogador + computador

    print("-" * 55)

    if soma % 2 == 0:
        resultado = "P"
        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR")
    else:
        resultado = "I"
        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR")
     
    print("-" * 55)

    if resultado == escolha_jogador:
        print("Você VENCEU!\n"
              "Vamos jogar novamente...")
        vitorias_jogador += 1
        continue
    else:
        print("Você PERDEU!")
        break

print(f"GAME OVER! Você venceu {vitorias_jogador} vez(es)")