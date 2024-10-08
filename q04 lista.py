def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: divisão por zero!"

def calculadora():
    print("Escolha a operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    escolha = input("Digite o número da operação desejada (1/2/3/4): ")
    
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        print(f"Resultado: {somar(n1, n2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(n1, n2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(n1, n2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(n1, n2)}")
    else:
        print("Escolha inválida!")

calculadora()
