# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario_original = float(input("Qual é o salário do funcionário? R$ "))

aumento = 15 / 100 * salario_original
novo_salario = salario_original + aumento

print(f"Um funcionário que ganhava R$ {salario_original}, com 15% de aumento, "
      f"passa a receber R$ {novo_salario:.2f}")