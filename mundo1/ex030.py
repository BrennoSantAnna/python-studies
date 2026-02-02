# Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input("Me diga um número qualquer: "))

if numero % 2 == 0:
    print(f"O número {numero} é \033[34mPAR!\033[m")
else:
    print(f"O número {numero} é \033[34mIMPAR\033[m")