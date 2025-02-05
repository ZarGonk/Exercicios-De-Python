#Exercício 78: Faça um programa que leia 5 valores numéricos e guarde-os 
#em uma lista. No final, mostre qual foi o maior e o menor valor digitado
#e as suas respectivas posições na lista.
'''numeros = []
for i in range(5):
    numeros.append(int(input(f'Digite {i+1}° valor: ')))

maior = max(numeros)
menor = min(numeros)

# Encontrando as posiçoes do menor valor
posicoes_maior = []
for i, num in enumerate(numeros):
    if num == maior:
        posicoes_maior.append(i + 1)

# Encontrando as posições do menor valor
posicoes_menor = []
for i, num in enumerate(numeros):
    if num == menor:
        posicoes_menor.append(i + 1)

print(f'O maior valor add foi: {maior} na posição {posicoes_maior}°')
print(f'O menor valor add foi: {menor} na posição {posicoes_menor}°')'''

#Exercício 79: Crie um programa onde o usuário possa digitar vários valores
#numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, 
#ele não será adicionado. No final, serão exibidos todos os valores únicos 
#digitados, em ordem crescente.
'''lista = []
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    else: 
        print('Valor ja existe!')
   
    while True:
        op = str(input('Deseja continuar[S/N] ? ')).strip().upper()[0]
        if op in ['S', 'N']:
            break
        else:
            print("Opção inválida! Digite 'S' para Sim ou 'N' para Não.")         
    if op == 'N':
        break

lista.sort()
print(lista)'''
         
#Exercício 80: Crie um programa onde o usuário possa digitar cinco valores
#numéricos e cadastre-os em uma lista, já na posição correta de inserção
#(sem usar o sort()). No final, mostre a lista ordenada na tela.
'''lista = []
for i in range(5):
    num = int(input(f'Digite {i} valor: '))
    
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista) and num > lista[posicao]:
            posicao += 1
        lista.insert(posicao, num)
print(lista)'''    

#Exercício 81: Crie um programa que vai ler vários números e colocar em uma
#lista. Depois disso, mostre:
#Quantos números foram digitados.
#A lista de valores, ordenada de forma decrescente.
#Se o valor 5 foi digitado e está ou não na lista.
'''lista = []
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
    print('Valor 5 não esta na lista')'''

#Exercício 82: Crie um programa que vai ler vários números e colocá-los em 
#uma lista. Depois disso, crie duas listas extras que vão conter apenas os 
#valores pares e os valores ímpares digitados, respectivamente. 
#Ao final, mostre o conteúdo das três listas geradas.
'''lista = [], pares = [] , impares = []
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
print(f'Impares Add: {impares}')'''

#Exercício 83: Crie um programa onde o usuário digite uma expressão qualquer 
#que use parênteses. Seu aplicativo deverá analisar se a expressão passada 
#está com os parênteses abertos e fechados na ordem correta.
exp = input('Digite sua Expressão: ')
pilha = []

for simb in exp:
  if simb == '(':
    pilha.append('(')
  elif simb == ')':
    if len(pilha) > 0:
      pilha.pop()
    else:
      pilha.append(')')
      break
if len(pilha) == 0:
  print('Sua Expressão esta Valida!')
else:
  print('Sua Expressão esta Invalida')