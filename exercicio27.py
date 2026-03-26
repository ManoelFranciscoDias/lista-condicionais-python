#entrada
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo  valor: '))
c = float(input('Digite o terceiro valor: '))

print("Escolha a opção:")
print("1 - Crescente")
print("2 - Decrescente")
print("3 - Maior do meio")

opcao = input('Informe qual opção você quer usar: ')

#processamento e saída

valores = [a, b, c]

if (opcao == "1"):
    valores.sort()
    print(f'Ordem crescente: {valores}')

elif (opcao == "2"):
    valores.sort(reverse=True)
    print(f'Ordem decrescente: {valores}')

elif (opcao == "3"):
    valores.sort()
    resultado = [valores[0], valores[2], valores[1]]
    print(f'O maior no meio: {resultado}')

else:
    print('Opção Invalida')
