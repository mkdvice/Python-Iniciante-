__author__ = '@MkDVice'

import math
import os

# programa para calcular equação do segundo grau

a = int(input('Digite o valor de A: '))   # Entrada do valor de A
b = int(input('Digite o valor de B: '))   # Entrada do Valor de B
c = int(input('Digite o valor de C: '))   # Entrada do valor de C

delta = int(math.pow(b, 2)) - (4 * a * c)          # Cálculo do valor do delta

print('''\n{}x² {}x {} = 0  \n'''.format(a, b, c)) # imprime a equação
print('Δ = b²-4*a*c')                          # imprime a fórmula de delta
print('Δ = {}² - 4*{}*{}'.format(b, a, c))     # imprime a resolução do delta
print('Δ = {} \n'.format(delta))               # imprime o valor de delta

if delta < 0:   # Condição para caso o denta de negativo
    print('Vázio, número inexistente no conjunto dos reais') # resultado se delta negativo
    os.system("pause") # Para o programa


x1 = float(-b + (math.sqrt(delta))) // 2 * a    # Cálculo de X linha
x2 = float(-b - (math.sqrt(delta))) // 2 * a    # Cálculo de X duas linhas

print('''x = (-b +- √∆) / (2 * a) \n''')        # imprime a fórmula de bhaskara
print('x = [-({}) + √{}] / (2 * a)'.format(b, delta, a))  # imprime a fórmula de bhaskara com valores para x linha
print('O valor de X linha é {}\n'.format(x1))   # imprime o valor de X linha

print('x = [-({}) - √{}] / (2 * a)'.format(b, delta, a))  # imprime a fórmula de bhaskara com valores para x duas linhas
print('O valor de x duas linhas {}'.format(x2)) # imprime o valor de X duas linhas
