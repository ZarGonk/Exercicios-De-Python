# Exercício 81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    lista.append(int(input('Enter a number: ')))

    while True:
        op = str(input('Want to continue[S/N]: ')).strip()[0]
        if op in 'SsNn':
            break
        else:
            print('Invalid Option. Sim (s) ou No (N): ')
    if op in 'Nn':
        break
total = len(lista)
print(f'Valor digitados: {total}')

lista.sort(reverse=True)
print(f'Lista na ordem decrescente: {lista}')

if 5 in lista:
    print('Valor 5 esta na lista')
else:
    print('Valor 5 não esta na lista')