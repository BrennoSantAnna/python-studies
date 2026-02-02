# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1. O nome com todas as letras maiúsculas e minúsculas
# 2. Quantas letras ao todo (sem considerar espaços)
# 3. Quantas letras tem o primeiro nome

# Função 'strip' utilizada para evitar espaços indevidos no início e final do nome
nome_completo = str(input("Digite seu nome completo: ")).strip()

nome_sem_espacos = nome_completo.replace(" ", "")
separador = nome_completo.split(" ")
primeiro_nome = separador[0]

print("Analisando seu nome...\n"
      f"Seu nome em maiúsculas é: {nome_completo.upper()}\n"
      f"Seu nome em minúsculas é {nome_completo.lower()}\n"
      f"Seu nome tem ao todo {len(nome_sem_espacos)} letras\n"
      f"Seu primeiro nome é {primeiro_nome} e ele tem {len(primeiro_nome)} letras")