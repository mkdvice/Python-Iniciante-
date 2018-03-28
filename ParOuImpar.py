__author__ = '@MkDVice'

# PROGRAMA PAR OU ÍMPAR

numero = int(input('Digite um número qualquer: ')) # entrada do número

resultado = numero % 2  # algoritimo para saber se é par ou impar

if resultado == 0:  # condição para mostrar se é par ou ímpar
    print('O número {} é PAR'.format(numero))   # mostra par
else:
    print('O número {} é ÍMPAR'.format(numero)) # mostra ímpar
