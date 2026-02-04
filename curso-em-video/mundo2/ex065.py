# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve
# perguntar ao usuário se ele quer ou não continuar a digitar valores

contagem_numeros = media = soma = maior_valor = menor_valor = 0

while True:
    numero = int(input("Digite um número: "))

    contagem_numeros += 1
    soma += numero
    media = soma / contagem_numeros
    
    if numero > maior_valor:
        maior_valor = numero
    else:
        menor_valor = numero

    opcao = str(input("Quer continuar? [S/N]: ")).upper()[0]

    if opcao == "S":
        continue
    elif opcao == "N":
        print(f"Você digitou {contagem_numeros} números e a média foi {media:.2f}\n"
              f"O maior valor foi {maior_valor} e o menor foi {menor_valor}")
        break
    else:
        print("Opção inválida! Tente novamente")