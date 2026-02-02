# Refaça o desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando o laço for

numero = int(input("Digite um número para ver sua tabuada: "))

for contador in range(1, 11):
    print(f"{numero} x {contador} = {numero * contador}")