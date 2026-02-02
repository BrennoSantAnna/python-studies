# Refaça o DESAFIO 035 dos triângulos, acresentando o recurso 
# de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: Todos os lados iguais
# ISÓSCELES: Dois lados iguais
# ESCALENO: Todos os lados diferentes

print("-=" * 13)
print("Analisador de Triângulos")
print("-=" * 13)

a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR triângulo ", end="")
    if a == b == c:
        print(f"EQUILÁTERO!")
    elif a != b != c != a:
        print(f"ESCALENO!")
    else:
        print(f"ISÓSCELES!")
else:
    print("Os segmentos NÃO PODEM FORMAR triângulo")