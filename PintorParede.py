largura = float(input('Digite o valor da largura da parede em metros: '))
altura = float(input('Digite o valor da altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('A sua parede tem as dimensões {:.2f}x{:.2f}, área da parede é {:.2f}M. Você gastara {:.2f}L para pintar a parede.'.format(largura, altura, area, tinta))
