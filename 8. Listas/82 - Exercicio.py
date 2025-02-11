# Exercício 82: Crie um programa que vai ler vários números e colocá-los em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.

lista = [], pares = [] , impares = []
i = 0
while True:
    lista.append(int(input('Enter a Number: ')))

    if lista[i] % 2 == 0:
         pares.append(lista[i])
    else:
        impares.append(lista[i])
    i += 1

    stop = ' '
    while stop not in 'SN':
        stop = input('Want to Stop[S/N]: ').strip().upper()[0]
    if stop == 'S':
        break 
     
lista.sort()
print(f'The initial list: {lista}')
print(f'Pares Add: {pares}')
print(f'Impares Add: {impares}')