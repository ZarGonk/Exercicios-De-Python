#Exercício 115: Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

#   O sistema deve ter um menu com opções de listar pessoas cadastradas, cadastrar nova pessoa e sair do sistema.
#   Use tratamento de erros para garantir que qualquer problema com o arquivo ou entrada do usuário seja tratado de forma adequada.
from lib import *
from arquivo import *
from time import sleep

arq = 'cadastro.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:

    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastra Nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Opção De ler o Arquivo Com As Pessoas Cadastradas
        lerArquivo(arq)
    elif resposta == 2:
        #Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do Sistema')
        break
    else:
        print('\033[31mERRO!!! Digite opção Válida: \033[m')
    sleep(1.5)