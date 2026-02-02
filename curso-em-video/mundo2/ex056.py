# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo, Quantas mulheres têm menos de 20 anos
# Qual é o nome do homem mais velho

media_idade = 0
mulheres_menos_20 = 0
maior_idade_homem = 0
homem_mais_velho = ""

for pessoa in range(1, 5):
    print(f"----- {pessoa}ª PESSOA  -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).upper()

    media_idade += idade / 4

    if pessoa == 1 and sexo == "M":
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo == "M" and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1
    
print(f"A média de idade do grupo é de {media_idade} anos\n"
      f"O homem mais velho tem {maior_idade_homem} anos e se chama {homem_mais_velho}\n"
      f"Ao todo {mulheres_menos_20} mulher(es) com menos de 20 anos")
