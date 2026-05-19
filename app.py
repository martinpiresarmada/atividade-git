def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisao por zero"
    return a / b

def menu():
    print("Calculadora")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    opcao = input("Escolha uma opcao: ")
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))

    if opcao == "1":
        print(somar(a, b))
    elif opcao == "2":
        print(subtrair(a, b))
    elif opcao == "3":
        print(multiplicar(a, b))
    elif opcao == "4":
        print(dividir(a, b))

menu()