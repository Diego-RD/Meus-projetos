
while True:
    valor1 = float(input("Digite um numero: "))
    operador = input("Digite um operador: ")
    valor2 = float(input("Digite o segundo numero?: "))
    validar = ['+','-','*','/']

    if operador in validar:
    
        if operador == '+':
            resultado = valor1 + valor2
            print(f"O Resultado da soma é: {resultado} ")
        elif operador == '-':
            resultado = valor1 - valor2
            print(f"O Resultado da subitração é: {resultado} ")
        elif operador == '*':
            resultado = valor1 * valor2
            print(f"O Resultado da multiplicação é: {resultado} ")
        elif operador == '/':
            resultado = valor1 / valor2
            print(f"O Resultado da divisao é: {resultado} ")
        parada = input("gostaria de fazer outra conta sim ou nao ?:  ").lower()

        if parada != 'sim':
            break
    else:
        print("Operador incoreto!")

      

    