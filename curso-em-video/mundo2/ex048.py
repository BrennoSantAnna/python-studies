# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500

soma = 0
multiplos_tres = 0

for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        multiplos_tres += 1

print(f"A soma de todos os {multiplos_tres} valores solicitados é {soma}")