# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os primeiros elemntos de uma Sequência de Fibbonacci
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

print("-" * 30)
print("Sequência de Fibbonacci")
print("-" * 30)

numero = int(input("Quantos termos você quer mostrar? "))

termo1 = 0
termo2 = 1

print("~" * 30)
print(f"{termo1} -> {termo2}", end="")

contador = 3

while contador <= numero:
    termo3 = termo1 + termo2
    print(f" -> {termo3}", end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
    
print(" -> FIM")
print("~" * 30)