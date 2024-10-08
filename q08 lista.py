def somar_elementos(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

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

    resultado = somar_elementos(lista_numeros)
    print(f"A soma dos elementos da lista é: {resultado}")
