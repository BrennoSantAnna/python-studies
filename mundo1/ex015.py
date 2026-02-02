# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$ 60 por dia e R$ 0.15 por km rodado

dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = int(input("Quantos Km rodados: "))

valor_total = (dias_alugados * 60) + (km_rodados * 0.15)

print(f"O total a pagar é de R$ {valor_total:.2f}")