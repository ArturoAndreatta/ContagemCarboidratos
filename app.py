from defs import *
from variaveis import *

# if escolha == 1:
#     print ('|----------- MENU ------------|')
#     print ('|                             |')
#     print ('| 1 - CALCULAR C/ Nº CARBO    |')
#     print ('| 2 - CALCULAR C/ ALIMENTO    |')
#     print ('|                             |')
#     print ('|-----------------------------|')
#     escolhaContCarbo = int(input('Qual opção deseja? '))
#     if escolhaContCarbo == 1:
#         PARTE EM QUE IRÁ CALCULAR COM NÚMERO DE CARBOIDRATO
#     if escolhaContCarbo == 2:
#         PARTE EM QUE IRÁ CALCULAR COM ALIMENTO

# if escolha == 2:
#     AQUI SERÁ A PARTE EM QUE TERÁ RELAÇÃO COM BANCO DE DADOS ONDE SERÁ NECESSÁRIO CADASTRAR O ALIMENTO

try:
    glicemia = int(input('Quanto está sua glicose? '))
except:
    print('Digite um valor numérico!')
correcao = (glicemia - 100)/40

if mostrarMenu() == 1:
    while alimento != '0':
        print ('')
        print (' __________________________ ')
        print ('|                          |')
        print ('|    LISTA DE ALIMENTOS    |')
        print ('|                          |')
        print ('| * pao frances            |')
        print ('| * shake                  |')
        print ('| * rap 10                 |')
        print ('|                          |')
        print ('| Para sair digite: 0      |')
        print ('|__________________________|')
        print ('')
        print (' ____________________________')
        print ('|    ALIMENTOS ESCOLHIDOS    |')
        print ('|                            |')
        for i in listaAlimentos:
            if i == 'pao frances':
                print ('| Pão Francês: {}             |'.format(totalPaoFrances))
            if i == 'shake':
                print ('| Shake: {}                   |'.format(totalShake))
            if i == 'rap 10':
                print ('| Rap 10: {}                  |'.format(totalRap10))
            
        print ('|                 TOTAL: {}   |'.format(len(listaAlimentos)))
        print ('|    TOTAL CARBOIDRATOS: {} |'.format(carbo))
        print ('|____________________________|')
        alimento = str(input('Qual alimento você deseja usar?'))

        if alimento == 'pao frances':
            carbo += 27
            if alimento not in listaAlimentos:
                listaAlimentos.append(alimento)
            totalPaoFrances += 1
            totalItemEscolhido = totalPaoFrances

        elif alimento == 'shake':
            carbo += 87
            if alimento not in listaAlimentos:
                listaAlimentos.append(alimento)
            totalShake += 1

        elif alimento == 'rap 10':
            carbo += 20
            if alimento not in listaAlimentos:
                listaAlimentos.append(alimento)
            totalRap10 += 1

        elif alimento != 'pao frances' and alimento != 'shake' and alimento != 'rap 10' and alimento != '0':
            print ('digite uma opção válida')

        elif alimento == '0':
            pass
    while escolha2 != 'não':
        escolha2 = str(input('Deseja adicionar mais carboidratos? Número atual: {} '.format(carbo)))

        if escolha2 == 'sim':
            maisCarbo = int(input('Deseja adicionar quantos carboidratos? '))
            carbo += maisCarbo
            print ('Carboidratos atuais: {}'.format(carbo))

        elif escolha2 == 'não':
            pass

        elif escolha2 != 'sim' and escolha2 != 'não':
            print ('Digite uma opção válida!')

else:
    carbo = int(input('Quantos carboidratos você ingeriu? '))
    
# SISTEMA PARA PEDIR QUAL HORÁRIO DO DIA A GLICOSE ESTÁ SENDO MEDIDA PARA DOSE DE INSULINA ADEQUADA
calcularInsulina(carbo, correcao)