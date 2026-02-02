# Escreva um programa que pergunte o salário de um funcionário 
# e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para salários inferiores ou iguais, o aumento é de 15%

salario_antigo = float(input("Qual é o salário do funcionário: R$ "))

if salario_antigo <= 1250:
    salario_novo = (0.15 * salario_antigo) + salario_antigo
else:
    salario_novo = (0.1 * salario_antigo) + salario_antigo

print(f"Quem ganhava R$ {salario_antigo:.2f} passa a ganhar R$ {salario_novo:.2f} agora")