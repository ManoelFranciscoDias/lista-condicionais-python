# entrada
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite o código da operação: "))

#processamento e saída
if operacao == 1:
    resultado = valor1 + valor2
    print("Resultado:", resultado)

elif operacao == 2:
    resultado = valor1 - valor2
    print("Resultado:", resultado)

elif operacao == 3:
    resultado = valor1 * valor2
    print("Resultado:", resultado)

elif operacao == 4:
    if valor2 != 0:
        resultado = valor1 / valor2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero!")

else:
    print("Operação inválida!")