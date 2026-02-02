# Faça um programa que mostre na tela uma contagem regressiva
# para o estouro de fogos de artifício, indo de 10 até 0, com
# pausa de 1 segundo entre eles

# Importação de módulos necessários para o funcionamento do programa
from time import sleep

for num in range(10, 1, -1):
    print(num)
    sleep(1)

print("BUM! BUM! POOOW!")