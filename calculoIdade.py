idade = int(input('Informe a sua idade: '))
if(idade<=0):
    print('A sua idade não pode ser 0 ou menor que 0! ')
else:
    if(idade>150):
        print('A sua idade não pode ser superior a 150 anos! ')
    else:
        if(idade<18):
            print('Você precisa ter mais de 18 anos! ')