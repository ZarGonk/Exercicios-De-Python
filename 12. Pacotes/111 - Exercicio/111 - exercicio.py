#Exercício 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos exercícios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionado.

from utilidadesCeV import moeda

preço = float(input('Digite o valor: R$ '))
moeda.resumo(preço, 20, 12)