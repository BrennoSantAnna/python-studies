# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo

numero = int(input("Digite um número: "))

total = 0

for contador in range(1, numero + 1):
    if numero % contador == 0:
        print(end="")
        total += 1
    else:
        print(end="")
    print(f"{contador} ", end="")

print(f"\nO número {numero} foi divisível {total} vezes")

if total == 2:
    print(f"E por isso ele é PRIMO!")
else:
    print(f"E por isso ele NÃO É PRIMO!")