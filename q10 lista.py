def calcular_media(lista):
    if not lista:
        return 0

    soma = sum(lista)
    media = soma / len(lista)
    return media

if __name__ == "__main__":
    lista_numeros = []
    while True:
        entrada = input("Digite um número (ou 'sair' para finalizar): ")
        if entrada.lower() == 'sair':
            break
        try:
            numero = float(entrada)
            lista_numeros.append(numero)
        except ValueError:
            print("Por favor, insira um número válido.")

    resultado = calcular_media(lista_numeros)
    print(f"A média dos números da lista é: {resultado}")
