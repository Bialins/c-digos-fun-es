def pn (num):
    if num > 0:
        print('positivo')
    elif num == 0:
        print('nulo')
    else:
        print('Negativo')
print('POSITIVO OU NEGATIVO')
num = int (input('Digite um número:'))
print('Este número é', end=' ')
pn(num)