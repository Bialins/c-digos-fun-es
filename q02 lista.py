def digitos(numero):
    return len(str(abs(numero)))


n = int(input('Digite um número inteiro: '))
print(f'O número {n} tem {digitos(n)} digitos')