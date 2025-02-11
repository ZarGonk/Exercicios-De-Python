# Exercício 79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
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
print(lista)  