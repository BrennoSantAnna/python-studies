# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# Importação de módulo necessário para o funcionamento do programa
from random import shuffle

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

# Ordenando a lista de alunos
shuffle(lista_alunos)
ordem_sorteada = lista_alunos

print(f"A ordem de apresentação será\n"
      f"{ordem_sorteada}")