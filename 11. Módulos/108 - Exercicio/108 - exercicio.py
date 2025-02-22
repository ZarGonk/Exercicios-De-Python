# Exercicio 108: Adapte o código do exercício anterior, criando uma função adicional chamada moeda() no módulo moeda.py, que consiga formatar um valor como um preço, exibindo o símbolo monetário (ex.: R$ 1.000,00).
import moeda

preço = float(input('Digite o valor: R$ '))

print(f'A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))}')
print(f'A dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'A aumento de {moeda.moeda(preço)} é {moeda.moeda(moeda.aumenta(preço, taxa=10))}')
print(f'A diminuir de {moeda.moeda(preço)} é {moeda.moeda(moeda.diminuir(preço,taxa=13))}') 