# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais 
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print("Gerador de PA")
print("-=" * 10)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f"{termo} -> ", end="")
    termo += razao
    contador += 1
    
print("ACABOU")