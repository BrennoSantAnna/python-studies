# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: R$ "))
salario_comprador = float(input("Salário do comprador: R$ "))
anos_pagamento = int(input("Em quantos anos vai pagar? "))

prestacao_mensal = valor_casa / (anos_pagamento * 12)
limite_prestacao = salario_comprador * 0.3

print(f"Para pagar uma casa de R$ {valor_casa:.2f} em {anos_pagamento} anos, a prestação mensal será de R$ {prestacao_mensal:.2f}")

if prestacao_mensal <= limite_prestacao:
    print("Empréstimo aprovado!")
else:
    print("Empréstimo negado!")