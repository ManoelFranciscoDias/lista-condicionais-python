# entrada
produto = float(input("Digite o preço do produto: "))

# processamento e saída
if produto < 20:
    print(f'O valor da venda do produto é R${produto * 1.45}.')

else:
    print(f'O valor da venda do produto é R${produto * 1.30}.')

