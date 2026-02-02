# Faça um programa que leia algo pelo teclado e mostre na tela o 
# seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(valor)}\n"
      f"Só tem espaços? {valor.isspace()}\n"
      f"É um número? {valor.isnumeric()}\n"
      f"É alfabético? {valor.isalpha()}\n"
      f"É alfanumérico? {valor.isalnum()}\n"
      f"Está em maiúsculas? {valor.isupper()}\n"
      f"Está em minúsculas? {valor.islower()}\n"
      f"Está capitalizada? {valor.istitle()}")