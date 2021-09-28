nome = (input('Por favor, digite seu nome: '))
real = float(input('Quanto você tem na carteira? R$ '))
dolar = real / 3.27
print('Senhor, {}. O valor quem você tem na carteira é de R${:.2f}, o valor convetido U${:.2f}'.format(nome, real, dolar))
