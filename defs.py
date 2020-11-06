from variaveis import *

def mostrarMenu():
    print (' _____________________________')
    print ('|                             |')
    print ('|            MENU             |')
    print ('|                             |')
    print ('| Adicionar alimento: 1       |')
    print ('| Número de carboidratos: 2   |')
    print ('|                             |')
    # print ('|   # ADICIONAR DEPOIS #      |')
    # print ('|                             |')
    # print ('|            MENU             |')
    # print ('|                             |')
    # print ('| 1 - CONTAGEM DE CARBOIDRATO |')
    # print ('| 2 - CADASTRAR ALIMENTO      |')
    # print ('|                             |')
    print ('|_____________________________|')
    escolha = int(input('Qual opção deseja? '))
    return escolha

def calcularInsulina(carbo, correcao):
    print (' _____________________________')
    print ('|                             |')
    print ('|            MENU             |')
    print ('|                             |')
    print ('|     Qual opção deseja?      |')
    print ('|                             |')
    print ('| 1 - Café da manhã           |')
    print ('| 2 - Almoço                  |')
    print ('| 3 - Lanche/Janta            |')
    print ('|                             |')
    print ('|_____________________________|')
    escolhaHora = int(input('Qual opção deseja? '))

    if escolhaHora == 1:
        print ('Você escolheu Café da manhã')
        insulina = (carbo/7) + correcao
        print (f'Aplicar {insulina:.2f} unidades de insulina')

    elif escolhaHora == 2:
        print ('Você escolheu Almoço')
        insulina = (carbo/7) + correcao
        print (f'Aplicar {insulina:.2f} unidades de insulina')

    elif escolhaHora == 1:
        print ('Você escolheu Lanche/Janta')
        insulina = (carbo/7) + correcao
        print (f'Aplicar {insulina:.2f} unidades de insulina')