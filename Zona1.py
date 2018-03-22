__author__ = '@MkDVice'

# SEPARADOR DÍGITOS DE UM NÚMERO

num = int(input('Informe um número: ')) # Leitura do número inteiro

u = num // 1 % 10       # Cálculo para obter unidade
d = num // 10 % 10      # Cálculo para obter dezena
c = num // 100 % 10     # Cálculo para obter centena
m = num // 1000 % 10    # Cálculo para obter milhar

print('Analisando o número {}'.format(num)) # mostra o número
print('Unidade: {}'.format(u))   # Mostra unidade
print('Dezena: {}'.format(d))    # Mostra dezena
print('Centena: {}'.format(c))   # Mostra centena
print('Milhar: {}'.format(m))    # Mostra milhar