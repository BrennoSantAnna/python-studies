# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número 
# entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer 

from random import randint

computador = randint(0, 10)

print("Sou seu computador...\n"
      "Acabei de pensar em um número entre 0 e 10.\n"
      "Será que você consegue advinhar qual foi?")

acertou = False
tentativas = 0

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    tentativas += 1

    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos... Tente mais uma vez.")
        elif jogador < computador:
            print("Mais... Tente mais uma vez.")

print(f"Acertou com {tentativas} tentativa(s)!")