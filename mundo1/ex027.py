# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente
# Ex. Ana Maria de Souza - primeiro = Ana - último = Souza

nome_completo = str(input("Digite seu nome completo: ")).strip()

# separando o nome em lista para acesssar o primeiro e último elemento
nome_separado = nome_completo.split()

print(f"Muito prazer em te conhecer!\n"
      f"Seu primeiro nome é {nome_separado[0]}\n"
      f"Seu último nome é {nome_separado[-1]}")