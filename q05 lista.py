def contar_vogais(s):
    vogais = "aeiouAEIOU"
    contador = 0

    for char in s:
        if char in vogais:
            contador += 1

    return contador

if __name__ == "__main__":
    string_input = input("Digite uma palavra: ")
    resultado = contar_vogais(string_input)
    print(f"Número de vogais na palavra é: {resultado}")
