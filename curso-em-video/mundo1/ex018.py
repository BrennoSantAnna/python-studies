# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

# Importação de módulos necessários para o funcionamento do programa
from math import radians, sin, cos, tan

angulo = int(input("Digite o ângulo que você deseja: "))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f"O ângulo de {float(angulo):.1f} tem o SENO de {seno:.2f}\n"
      f"O ângulo de {float(angulo):.1f} tem o COSSENO de {cosseno:.2f}\n"
      f"O ângulo de {float(angulo):.1f} tem a TANGENTE de {tangente:.2f}")