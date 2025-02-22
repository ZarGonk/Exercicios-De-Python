# Exercício 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas:

# aumentar(preço, taxa)
# diminuir(preço, taxa)
# dobro(preço)
# metade(preço)
#Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda

preço = float(input('Digite o valor: R$ '))

print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'A dobro de {preço} é {moeda.dobro(preço)}')
print(f'A aumento de {preço} é {moeda.aumenta(preço, taxa=10)}')
print(f'A diminuir de {preço} é {moeda.diminuir(preço,taxa=13)}') 