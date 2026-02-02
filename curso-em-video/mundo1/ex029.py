# Escreva um programa que leia a velocidade um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar
# R$ 7,00 por cada Km acima do limite

velocidade_atual = int(input("Qual é a velocidade atual do carro? "))

VELOCIDADE_PERMITIDA = 80
multa = 0

if velocidade_atual > VELOCIDADE_PERMITIDA:
    multa = (velocidade_atual - VELOCIDADE_PERMITIDA) * 7
    print(f"\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h\n"
          f"Você deve pagar uma multa de\033[m \033[33mR$ {multa:.2f}!\033[m\n"
          f"\033[32mTenha um bom dia! Dirija com segurança!\033[m")
else:
    print(f"\033[32mTenha um bom dia! Dirija com segurança!\033[m")