# Faça um programa que leia o ano de nascimento de um jovem e informem,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou
# do prazo

# Importação de módulos necessários para o funcionamento do programa
from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade_atual = ano_atual - ano_nascimento
anos_restantes = 0
anos_passados = 0

print(f"Quem nasceu em {ano_nascimento} tem {idade_atual} em {ano_atual}.")

if idade_atual < 18:
    anos_restantes = 18 - idade_atual
    print(f"Ainda faltam {anos_restantes} anos para o alistamento\n"
          f"Seu alistamento será em {ano_atual + anos_restantes}.")
elif idade_atual > 18:
    anos_passados = idade_atual - 18
    print(f"Você já deveria ter se alistado há {anos_passados} ano(s).\n"
          f"Seu alistamento foi em {ano_atual - anos_passados}.")
else:
    print(f"Você tem que se alistar IMEDIAMENTE")