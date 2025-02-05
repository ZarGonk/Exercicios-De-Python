#1.Concatenar listas:
# -Crie duas listas separadas com elementos numéricos.
# -Depois, una essas duas listas em uma única lista.
# -Finalmente, exiba a lista resultante na tela.
'''lista1 = [1, 3 ,5 ,7 ,9]
lista2 = [2, 4, 6, 8, 10]
conc = lista1 + lista2

conc.sort()
print(conc)'''

#2.Buscar elemento na lista:
# -Inicie com uma lista de números.
# -Escolha um número específico que deseja buscar na lista.
# -Verifique a presença desse número na lista e exiba uma mensagem 
# confirmando se ele está presente ou não.
'''numeros = [1, 2, 5, 6, 8, 3, 4, 9, 13]
count = 0
if 3 in numeros:
    print(f'Numero encontrado {numeros.count(3)} vezes\nNa posição',end=' ')
    for n in numeros:
        count += 1
        if n == 3:
            print(count, end='...')
else:
    print('Numero nao encontrado')'''

#3.Modificar elementos da lista:
# -Crie uma lista contendo várias palavras.
# -Identifique a posição da palavra que deseja modificar 
# (por exemplo, a segunda posição).
# -Substitua essa palavra por uma nova palavra de sua escolha.
# -Exiba a lista antes e depois da modificação para verificar a mudança.
'''palavras = ['Arroz', 'Feijao', 'Gustavo', 'Carro']
print(palavras)

palavras.remove('Feijao')
palavras.insert(1, 'Nao_Existe_mais')

print(palavras)'''

#4.Contar elementos na lista
# -Crie uma lista com diversos números, incluindo repetições.
# -Escolha um número específico cujo total de aparições você deseja contar.
# -Conte quantas vezes esse número aparece na lista.
# -Exiba o número escolhido e a contagem de suas ocorrências na lista.
'''from random import randint
numeros = []
for i in range(8):
    num = randint(1, 10)
    numeros.append(num)
enc = int(input('Qual numero deseja verificar: '))
print(f'O seu numero {enc} teve a ocorrencia de {numeros.count(enc)}')'''

#5.Remover elementos específicos
# -Crie uma lista com vários números.
# -Escolha um número que deseja remover de todas as posições onde 
# ele aparece.
# -Percorra a lista e remova todas as ocorrências desse número.
# -Exiba a lista após a remoção para confirmar que o número foi eliminado
numeros = [1, 2, 3, 2, 4, 5, 2, 6]
print(f"Lista original: {numeros}")

numero_a_remover = 2
while numero_a_remover in numeros:
    numeros.remove(numero_a_remover)

print(f"Lista após remover {numero_a_remover}: {numeros}")
