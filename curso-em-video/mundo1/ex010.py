# Crie um prograrma que leia quanti dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar. Considere U$ 1.00 = R$ 3.27

valor_carteira = float(input("Quanto dinheiro você tem na carteira? R$ "))

print(f"Com R$ {valor_carteira} você pode comprar US$ {valor_carteira / 3.27:.2f}")