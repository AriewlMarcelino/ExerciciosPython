# Exercicio de logica 1 - Fatura

import os


repetir = 's'
x = 0
total = 0
fatura = []
produtos = []

print('======================================================')
print('=        SISTEMA DE COMPRAS SEJA-BEM VINDO           =')
print('======================================================')

while repetir == 's':

    nome = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o preço: '))

    # Adicionando valor do produto ao cliente: ok
    fatura.append(precoProduto)
    x += 1
    print(fatura)

    # Somando valores dos produtos do cliente: ok
    for i in fatura:
        total += i
        os.system('cls') or None
        print('Ultimo produto adicionado: ',
              'Produto:', nome, '| valor:', precoProduto)
        print('A sua fatura esta em: ', total)

        repetir = input('Deseja continuar a comprando ?')
        print('...')


print('======================================================')
print('=                    VOLTE SEMPRE                    =')
print('======================================================')

# mostrando para o usuario o resultado da compra
print('A sua fatura é: ', total)
