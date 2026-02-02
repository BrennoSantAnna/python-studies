# Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

decimo_valor = primeiro_termo + (10 - 1) * razao

for contador in range(primeiro_termo, decimo_valor + razao, razao):
    print(f"{contador}", end=" > ")

print("Acabou")