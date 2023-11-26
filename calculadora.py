

# Projeto de calculadora sem uso de biblioteca

numero1 = float(input("Digite o primeiro numero: "))
operador = input("Digite um operador: ")
numero2 = float(input("Digite segundo numero: "))

if operador == '+':
    resultado = numero1 + numero2
    print(f"Seu resultado é : {resultado}")
elif operador == '-':
    resultado = numero1 - numero2
    print(f"Seu resultado é : {resultado}")
elif operador == '*':
    resultado = numero1 * numero2
    print(f"Seu resultado é : {resultado}")
elif operador == '/':
    resultado = numero1 / numero2
    print(f"Seu resultado é : {resultado}")

else:
    print("Operador incorreto tente denovo!")








