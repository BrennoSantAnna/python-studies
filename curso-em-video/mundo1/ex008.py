# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

distancia_metros = int(input("Uma distância em metros: "))

print(f"A medida de {float(distancia_metros)}m corresponde a \n"
      f"{distancia_metros / 1000}km\n"
      f"{distancia_metros / 100}hm\n"
      f"{distancia_metros / 10}dam\n"
      f"{distancia_metros * 10}dm\n"
      f"{distancia_metros * 100}cm\n"
      f"{distancia_metros * 1000}mm")