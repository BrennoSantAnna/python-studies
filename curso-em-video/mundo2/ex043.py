# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso - Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso - Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Qual seu peso? (Kg) "))
altura = float(input("Qual sua altura? (m) "))

imc = peso / (altura * altura)

if imc <= 18.5:
    resultado = "ABAIXO DO PESO"
elif imc > 18.5 and imc <= 25:
    resultado = "PESO IDEAL"
elif imc > 25 and imc <= 30:
    resultado = "SOBREPESO"
elif imc > 30 and imc <= 40:
    resultado = "OBESIDADE"
else:
    resultado = "OBESIDADE MÓRBIDA"

print(f"O IMC dessa pessoa é de {imc:.1f}\n"
      f"Situação: {resultado}")