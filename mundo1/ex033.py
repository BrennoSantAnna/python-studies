# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

menor_valor = a

if b < a and b < c:
    menor_valor = b
if c < a and c < b:
    menor_valor = c

maior_valor = a

if b > a and b > c:
    maior_valor = b
if c > a and c > b:
    maior_valor = c

print(f"O menor valor digitado foi {menor_valor}\n"
      f"O maior valor digitado foi {maior_valor}")