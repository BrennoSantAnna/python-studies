# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
numeros_pares = 0

for contador in range(1, 7):
    numero = int(input(f"Digite o {contador}º valor: "))
    if numero % 2 == 0:
        soma += numero
        numeros_pares += 1
    
print(f"Você digitou {numeros_pares} número(s) par(es) e a soma é igual a {soma}")