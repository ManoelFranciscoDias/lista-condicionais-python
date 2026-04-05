homem01 = int(input('Digite a idade do primeiro homem: '))
homem02 = int(input('Digite a idade do segundo homem: '))
mulher01 = int(input('Digite a idade da primeira mulher: '))
mulher02 = int(input('Digite a idade da segunda mulher: '))

if homem01 > homem02 and mulher01 > mulher02:
    soma = homem01 + mulher02
    produto = homem02 * mulher01

elif homem01 > homem02 and mulher02 > mulher01:
    soma = homem01 + mulher01
    produto = homem02 * mulher02

elif homem02 > homem01 and mulher01 > mulher02:
    soma = homem02 + mulher02
    produto = homem01 * mulher01

else:
    soma = homem02 + mulher01
    produto = homem01 * mulher02

print(f"Soma: {soma}")
print(f"Produto: {produto}")