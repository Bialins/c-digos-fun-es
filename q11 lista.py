def converter_temperatura(valor, unidade):
    if unidade.lower() == 'c':
        return (valor * 9/5) + 32, 'F'
    elif unidade.lower() == 'f':
        return (valor - 32) * 5/9, 'C'
    else:
        return 'unidade inválida'

if __name__ == "__main__":
    temperatura = float(input("Digite a temperatura: "))
    unidade = input("Digite a unidade (C para Celsius, F para Fahrenheit): ")

    resultado = converter_temperatura(temperatura, unidade)

    if resultado != 'unidade inválida':
        print(f"A temperatura convertida é: {resultado[0]}°{resultado[1]}")
    else:
        print("Unidade inválida. Use 'C' para Celsius ou 'F' para Fahrenheit.")
