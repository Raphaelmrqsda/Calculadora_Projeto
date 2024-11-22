# Entrada do usuário
print("\n\nEntra: \n+ para adição \n- para subtração \n* para multiplicação \n/ para divisão")

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
escolha = input('Escolha a operação (+, -, *, /): ')

    # Soma
if escolha == '+':
    print("O Resultado é: ", num1 + num2)

    # subtração
if escolha == '-':
    print("O Resultado é: ", num1 - num2)

    # multiplicação
if escolha == '*':
    print("O Resultado é: ", num1 * num2)

    # divisão
if escolha == '/':
    print("O Resultado é: ", num1 / num2)


