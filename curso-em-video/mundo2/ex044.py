# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de desconto
# em até 2x no cartão preço normal - 3x ou mais no cartão: 20% de juros

preco_compras = float(input("Preço das compras: R$ "))

print("FORMAS DE PAGAMENTO\n"
      f"[ 1 ] à vista dinheiro/cheque/pix\n"
      f"[ 2 ] à vista cartão\n"
      f"[ 3 ] 2x no cartão\n"
      f"[ 4 ] 3x ou mais no cartão")

forma_pagamento = int(input("Qual a forma de pagamento? "))

desconto = 0
juros = 0
valor_total = 0
quantidade_parcelas = 0
valor_parcelas = 0

if forma_pagamento == 1:
    desconto = 0.1 * preco_compras
    valor_total = preco_compras - desconto
    print(f"Sua compra de R$ {preco_compras:.2f} vai custar R$ {valor_total:.2f} no final")

elif forma_pagamento == 2:
    desconto = 0.05 * preco_compras
    valor_total = preco_compras - desconto
    print(f"Sua compra de R$ {preco_compras:.2f} vai custar R$ {valor_total:.2f} no final")

elif forma_pagamento == 3:
    valor_parcelas = preco_compras / 2
    print(f"Sua compra será parcelada em 2x de R$ {valor_parcelas:.2f} SEM JUROS\n"
          f"Sua compra de R$ {preco_compras:.2f} vai custar R$ {preco_compras:.2f} no final")
    
elif forma_pagamento == 4:
    quantidade_parcelas = int(input("Quantas parcelas? "))
    juros = 0.2 * preco_compras
    valor_parcelas = (preco_compras + juros) / quantidade_parcelas
    print(f"Sua compra será parcelada em {quantidade_parcelas}x de R$ {valor_parcelas:.2f} COM JUROS\n"
          f"Sua compra de R$ {preco_compras:.2f} vai custar R$ {preco_compras + juros:.2f} no final")
    
else:
    print("Opção inválida! Tente novamente")