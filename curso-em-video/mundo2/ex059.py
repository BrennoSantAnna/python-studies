# Crie um programa que leia dois valores e mostre um menu
# Seu programa deverá realizar a operação solicitada em cada acesso
# [1] somar - [2] multiplicar - [3] maior - [4] novos números - [5] sair do programa

from time import sleep

primeiro_valor = int(input("Primeiro valor: "))
segundo_valor = int(input("Segundo valor: "))

opcao = 0

while opcao != 5:
    sleep(1)
    print("[ 1 ] somar\n"
        "[ 2 ] multiplicar\n"
        "[ 3 ] maior\n"
        "[ 4 ] novos números\n"
        "[ 5 ] sair do programa")

    opcao = int(input(">>>>> Qual é a sua opção? "))

    if opcao == 1:
        print(f"A soma entre {primeiro_valor} + {segundo_valor} é {primeiro_valor + segundo_valor}")

    elif opcao == 2:
        print(f"A multiplicação entre {primeiro_valor} x {segundo_valor} é {primeiro_valor * segundo_valor}")

    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            maior = primeiro_valor
        else:
            maior = segundo_valor
        print(f"Entre {primeiro_valor} e {segundo_valor} o maior valor é {maior}")

    elif opcao == 4:
        print("Informe os números novamente:")
        primeiro_valor = int(input("Primeiro valor: "))
        segundo_valor = int(input("Segundo valor: "))

    elif opcao == 5:
        print("Finalizando...")
        break

    else:
        print("Opção inválida. Tente novamente")
        
    print("=-=" * 11)

sleep(2)
print("=-=" * 11)
print("Fim do programa! Volte sempre!")