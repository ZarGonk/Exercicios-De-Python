#Exercício 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []
for i in range(5):
    num = int(input(f'Digite {i} valor: '))
    
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        posicao = 0
        while posicao < len(lista) and num > lista[posicao]:
            posicao += 1
        lista.insert(posicao, num)
print(lista)    