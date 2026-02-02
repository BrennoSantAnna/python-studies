# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

primeira_nota = float(input("1ª nota: "))
segunda_nota = float(input("2ª nota: "))

media = (primeira_nota + segunda_nota) / 2.0

print(f"A média entre {primeira_nota} e {segunda_nota} é igual a {media:.1f}")