# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menos peso lidos

maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f"Peso da {p}ª pessoa: "))

    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f"O maior peso lido foi de KG {maior_peso:.1f}\n"
      f"O menor peso lido foi de KG {menor_peso:.1f}")