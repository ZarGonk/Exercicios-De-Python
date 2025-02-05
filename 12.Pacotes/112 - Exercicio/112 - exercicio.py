#Exercício 112: #Dentro do pacote utilidadesCeV que criamos no desafio 111 temos um modulo chamado "dado". Crie também uma função chamada leiaDinheiro() no módulo dado, que seja capaz de funcionar como a função input(), mas com uma validação para aceitar apenas valores monetários.
#from utilidadesCeV import dado
from utilidadesCeV import moeda
from utilidadesCeV import dado

preço = dado.leiaDinheiro('Digite o valor: R$ ')
moeda.resumo(preço, 20, 12)