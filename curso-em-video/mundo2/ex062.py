# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais 
# alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos

print("Gerador de PA")
print("-=" * 10)

primeiro_termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

termo = primeiro_termo
contador = 1
termos_totais = 0
termos_a_mais = 10

while termos_a_mais != 0:
    termos_totais += termos_a_mais
    while contador <= termos_totais:
        print(f"{termo} -> ", end="")
        termo += razao
        contador += 1
    print("PAUSA")
    termos_a_mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com {termos_totais} termos mostrados")