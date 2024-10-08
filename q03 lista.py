
def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Erro,divisão por zero!"


def calculadora_completa():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    print(f"\nResultados para os números {num1} e {num2}:")
    print(f"Soma: {somar(num1, num2)}")
    print(f"Subtração: {subtrair(num1, num2)}")
    print(f"Multiplicação: {multiplicar(num1, num2)}")
    print(f"Divisão: {dividir(num1, num2)}")

calculadora_completa()

