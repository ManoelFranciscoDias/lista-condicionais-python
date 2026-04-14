#entrada
print("=== CALCULADORA ===")
print("0 - Soma")
print("1 - Subtração")
print("2 - Multiplicação")
print("3 - Divisão")
print("4 - Média")

opcao = int(input("Escolha uma opção (0 a 4): "))

#processamento e saída
if opcao >= 0 and opcao <= 4:
    n1 = float(input("Digite o primeiro número: ").replace(",", "."))
    n2 = float(input("Digite o segundo número: ").replace(",", "."))

    if opcao == 0:
        print(f"Soma: {n1 + n2}")

    elif opcao == 1:
        print(f"Subtração: {n1 - n2}")

    elif opcao == 2:
        print(f"Multiplicação: {n1 * n2}")

    elif opcao == 3:
        if n2 != 0:
            print(f"Divisão: {n1 / n2}")
        else:
            print("Erro: divisão por zero")

    elif opcao == 4:
        print(f"Média: {(n1 + n2) / 2}")

else:
    print("Valor errado. Programa encerrado sem cálculos")