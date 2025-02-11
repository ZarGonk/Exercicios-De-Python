#Exercício 109: Modifique as funções que você criou no exercício 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado deve ou não ser formatado pela função moeda(), desenvolvida no exercício 108.
import modulos

preço = float(input('Digite o valor: R$ '))

print(f'A metade de {modulos.moeda(preço)} é {modulos.metade(preço, True)}')
print(f'A dobro de {modulos.moeda(preço)} é {modulos.dobro(preço, True)}')
print(f'A aumento de {modulos.moeda(preço)} é {modulos.aumenta(preço, 10, True)}')
print(f'A diminuir de {modulos.moeda(preço)} é {modulos.diminuir(preço, 13, True)}')