def fatorial(n):
    if n < 0:
        return "O número deve ser um inteiro não negativo."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    numero_input = int(input("Digite um número inteiro não negativo: "))
    resultado = fatorial(numero_input)
    print(f"O fatorial de {numero_input} é {resultado}.")
