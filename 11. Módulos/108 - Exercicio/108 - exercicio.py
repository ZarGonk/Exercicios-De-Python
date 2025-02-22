# Exercicio 108: Adapte o código do exercício anterior, criando uma função adicional chamada moeda() no módulo moeda.py, que consiga formatar um valor como um preço, exibindo o símbolo monetário (ex.: R$ 1.000,00).
import modulos

preço = float(input('Digite o valor: R$ '))

print(f'A metade de {modulos.moeda(preço)} é {modulos.moeda(modulos.metade(preço))}')
print(f'A dobro de {modulos.moeda(preço)} é {modulos.moeda(modulos.dobro(preço))}')
print(f'A aumento de {modulos.moeda(preço)} é {modulos.moeda(modulos.aumenta(preço, taxa=10))}')
print(f'A diminuir de {modulos.moeda(preço)} é {modulos.moeda(modulos.diminuir(preço,taxa=13))}') 