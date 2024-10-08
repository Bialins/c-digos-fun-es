def contar_palavras(s):
    contador = 0
    em_palavra = False 

    for char in s:
        if char != ' ' and char != '\n' and char != '\t': 
            if not em_palavra:
                contador += 1 
                em_palavra = True
        else:
            em_palavra = False  

    return contador

if __name__ == "__main__":
    string_input = input("Digite uma ou mais palavras: ")
    resultado = contar_palavras(string_input)
    print(f"Número de palavras é: {resultado}")
