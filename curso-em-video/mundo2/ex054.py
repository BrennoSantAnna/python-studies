# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores

# Módulo necessário para o funcionamento do programa
from datetime import date

ano_atual = date.today().year
maiores_idade = 0
menores_idade = 0

for contador in range(1, 8):
    ano_nascimento = int(input(f"Em que ano a {contador}ª pessoa nasceu? "))
    if ano_atual - ano_nascimento >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1
    
print(f"\nAo todo tivemos {maiores_idade} pessoas maiores de idade\n"
      f"E também tivemos {menores_idade} pessoas menores de idade")