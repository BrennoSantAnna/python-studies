# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km
# para viagens de até 200Km e R$ 0,45 para viagens mais longas

distancia = int(input("Qual é a distância da sua viagem? "))

if distancia <= 200:
    preco = 0.5
else:
    preco = 0.45

valor = distancia * preco

print(f"Você está prestes a começar uma viagem de {float(distancia)}Km.\n"
      f"E o preço da sua passagem será de R$ {valor:.2f}")