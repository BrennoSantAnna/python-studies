# A confederação Nacional de Natação precisa de um programa que leia o ano 
# de nascimento de um atleta e mostre sua categoria, de acordo com sua idade
# Até 9 anos: MIRIM - Até 14 anos: INFANTIL - Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR - Acima: MASTER

# Importação de módulos necessários para o funcionamento do programa
from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year

idade_atleta = ano_atual - ano_nascimento

if idade_atleta <= 9:
    classificacao = "MIRIM"
elif idade_atleta >= 10 and idade_atleta <= 14:
    classificacao = "INFANTIL"
elif idade_atleta >= 15 and idade_atleta <= 19:
    classificacao = "JUNIOR"
elif idade_atleta >= 20 and idade_atleta <= 25:
    classificacao = "SÊNIOR"
else:
    classificacao = "MASTER"

print(f"O atleta tem {idade_atleta} anos.\n"
      f"Classificação: {classificacao}")