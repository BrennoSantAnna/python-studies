# Crie um algoritmo que leia um número e mostre o seu dobro, tripo e a raíz quadrada

# Importação da biblioteca math para uso da função sqrt
from math import sqrt

numero = int(input("Digite um número: "))

print(f"O dobro de {numero} vale {numero * 2}\n"
      f"O tripo de {numero} vale {numero * 3}\n"
      f"A raiz quadrada de {numero} vale {sqrt(numero):.2f}")