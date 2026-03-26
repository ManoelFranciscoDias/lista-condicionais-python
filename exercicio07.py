# entrada
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

# processamento e saída
if ano_nascimento > 2026:
    print('Sua idade é invalida')

else: 
    print(f"Seu ano é valido, você possuiu {2026 - ano_nascimento} anos")

