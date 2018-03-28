__author__="@MkDVice"

# calculo para custo de viagem

distancia = float(input('Quantos quilometros terá sua viagem? '))   # entrada de quilometros

print('Você está prestes a iniciar um viagem de {}Km'.format(distancia))    # mostra distancia

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
'''calc para determinar preço da viajem. Preço promocional para viajens acima de 200km '''

print('O valor da viagem será de R${:.2f}'.format(preco))   # exibe preço