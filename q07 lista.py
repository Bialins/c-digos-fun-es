def verificar_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numero_input = int(input("Digite um número: "))
    resultado = verificar_primo(numero_input)
    if resultado:
        print(f"{numero_input} é primo.")
    else:
        print(f"{numero_input} não é primo.")

