# Crie um programa que leia uma frase qualquer e diga 
# e ela é um palíndromo, desconsiderando os espaços
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA
# O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA

frase = str(input("Digite uma frase: ")).strip().upper()

palavras = frase.split()
palavras_juntas = "".join(palavras)
inverso = ""

for letra in range(len(palavras_juntas) -1, -1, -1):
    inverso += palavras_juntas[letra]

if inverso == palavras_juntas:
    print("Temos um palíndromo!")
else:
    print("A frase digitada não é um palíndromo!")