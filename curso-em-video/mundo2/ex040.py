# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final, de acordo com a média atingida
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média entre 7.0 ou superior: APROVADO

primeira_nota = float(input("Primeira nota: "))
segunda_nota = float(input("Segunda nota: "))

media = (primeira_nota + segunda_nota) / 2.0

if media < 5.0:
    situacao = "\033[1;31mREPROVADO\033m"
elif media >= 5.0 and media <= 6.9:
    situacao = "\033[1;33mRECUPERAÇÃO\033m"
else:
    situacao = "\033[1;32mAPROVADO\033m"

print(f"Tirando {primeira_nota} e {segunda_nota}, a média do aluno é {media}\n"
      f"O aluno está {situacao}.")