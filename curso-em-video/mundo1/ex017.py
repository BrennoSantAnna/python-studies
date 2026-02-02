# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um 
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Importação da biblioteca math para uso da função hypot
from math import hypot

cateto_oposto = float(input("Comprimento do cateto oposto: "))
cateto_adjacente = float(input("Comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")