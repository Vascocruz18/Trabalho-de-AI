# Função para soma
def soma(x, y):
    return x + y

# Função para subtracao
def subtracao(x, y):
    return x - y

# Função para multiplicacao
def multiplicacao(x , y):
    return x * y

# Função para divisao
def divisao(x, y):
    return x / y

# Função principal
def calculadora():

    while True:
        operador = input("Digite a operação: ")

        if operador != "hist":
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
        if operador == "soma":
            result = soma(num1, num2)
            print("resultado da soma: " + str(result))
        elif operador == "subtracao":
            result = subtracao(num1, num2)
            print("resultado da subtracao: " + str(result))
        elif operador == "multiplicacao":
            result = multiplicacao(num1, num2)
            print("resultado da multiplicacao: " + str(result))
        elif operador == "divisao":
            result = divisao(num1, num2)
            print("resultado da divisao: " + str(result))
        else:
            print("operação não suportada")
