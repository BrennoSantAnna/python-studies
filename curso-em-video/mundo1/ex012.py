# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_original = float(input("Qual é o preço do produto? "))

desconto = 5 / 100 * preco_original
novo_preco = preco_original - desconto

print(f"O produto que custava R$ {preco_original}, " 
      f"na promoção com desconto de 5% vai custar R$ {novo_preco:.2f}")