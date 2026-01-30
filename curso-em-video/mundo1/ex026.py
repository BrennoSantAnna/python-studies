# Faça um programa que leia uma frase pelo teclado e mostre:
# 1. Quantas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez

frase = str(input("Digite uma frase: ")).strip().upper()

print(f"A letra A aparece {frase.count("A")} vezes na frase\n"
      f"A primeira letra A apareceu na posição {frase.find("A") + 1}\n"
      f"A última letra A apareceu na posição {frase.rfind("A") + 1}")
