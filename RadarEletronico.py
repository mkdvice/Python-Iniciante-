__author__ = '@MkDVice'

# PROGRAMA RADAR ELETRONICO

velocidade = float(input('Qual é a velocidade atual do carro? '))   # ENTRADA DO VALOR DA VELOCIDADE

if velocidade > 80: # CONDIÇÃO PARA VELOCIDADE
    print('\nMULTADO! Você excedeu o limite de velocidade, que é de 80Km/h')    # AVISO DE MULTA
    multa = (velocidade - 8) * 7    # CALCULO PARA MULTA
    print('Você deve pagar uma multa de R${:.2f}!\n'.format(multa)) # VALOR DA MULTA

print('Tenha um bom dia! Dirija com cuidado!') # AVISO DE BOM DIA