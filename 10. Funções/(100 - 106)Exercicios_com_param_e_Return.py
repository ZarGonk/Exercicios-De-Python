

def ex102():
#Exercício 102: Crie um programa que tenha uma função chamada fatorial(), que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não o processo de cálculo do fatorial.
#   Exemplo:
#   fatorial(5, show=True)
#   Saída: 5 x 4 x 3 x 2 x 1 = 120
    def fatorial(num, show=True):
        """
        -> Calcula o fatorial de um numero.
        :param num: Numero a ser fatorado
        :param show: (opcional) Mostra ou não a conta
        :return: O valor do fatorial de um numero num.
        """
        fat = 1
        for i in range(num, 0, -1):
            if show == True:
                print(i, end= '')
                if i > 1:
                    print(' x', end=' ')
                else:
                    print(' =',end=' ')
            fat *= i
        return fat
    
    valor = int(input('Enter the value: '))
    print(fatorial(valor))

def ex103():
#Exercício 103: Crie um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
    def ficha(nome='', gols=0):
        if not nome:
            nome = '<Desconhecido>'
        return f'O jogador {nome} fez {gols} gol(s) no campeonato'
    
    nome = str(input('Nome do jogador: ')).strip().capitalize()

    gols = input('Numero de gols: ')
    if gols.isnumeric():  # Verifica se a entrada é numérica
        gols = int(gols)
    else:
        gols = 0
    print(ficha(nome, gols))

def ex104():
#Exercício 104: Crie um programa que tenha a função chamada leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#   Exemplo:
#n = leiaInt('Digite um número: ')
    def leiaInt(msg):
        ok = False
        valor = 0
        
        while True:
            n = input(msg)
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('\033[0;31mERRO! Digite um numero válido.\033[m')
            if ok == True:
                break
        return valor
    

    #Codigo principal
    n = leiaInt('Digite um numero: ')
    print(f'Voce acabou de digitar: {n}')

def ex105():
#Exercício 105: Faça um programa que tenha uma função chamada notas(), que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#Quantidade de notas.
#A maior nota.
#A menor nota.
#A média da turma.
#A situação (opcional), que pode ser: "boa", "razoável" ou "ruim".
    def notas(*nota, sit=False):
        """
        ->Função analisa notas e situacão de um aluno
        :param *nota: uma ou mais notas de um aluno (aceita varias)
        :param sit: Valor opcional, Indica a situação que se encontra o aluno
        :return: Dicionario com as informações registradas do aluno
        """
        boletim = dict()
        boletim["Total"] = len(nota)
        boletim["Maior"] = max(nota)
        boletim["Menor"] = min(nota)
        boletim["Media"] = sum(nota)/ len(nota)

        if sit == True:
            if boletim['Media'] > 7:
                boletim["Situação"] = 'BOA'
            elif 6 <= boletim['Media'] < 7:
                boletim['Situação'] = 'RAZOAVEL'
            else:
                boletim['Situação'] = 'RUIM'
        return boletim

    resp = notas(2.5, 1.5, 2)
    print(resp)

def ex106():
    """
    Mini-sistema de ajuda interativo usando o Interactive Help do Python.
    O usuário pode digitar um comando ou função para exibir sua documentação.
    O programa termina quando o usuário digitar 'FIM'.
    """
    # Definição de cores
    cores = [
        '\033[m',      # Reset color
        '\033[0;31m',  # Letras Vermelhas
        '\033[0;34m',  # Letras Azuis
        '\033[7;30m',  # Fundo Branco
    ]

    def ajuda(comando):
        """
        Exibe o manual de um comando ou biblioteca com estilização.
        """
        titulo(f"Acessando o manual do comando '{comando}'", 2)
        
        print(cores[3], end='')  # Fundo branco
        help(comando)
        print(cores[0], end='')  # Reset

    def titulo(msg, cor=0):
        """
        Exibe um título formatado com bordas e cor.
        :param msg: Texto do título.
        :param cor: Índice da cor na lista 'cores'.
        """
        tam = len(msg) + 4
        print(cores[cor], end='')
        print('~' * tam)
        print(f"  {msg}")
        print('~' * tam)
        print(cores[0], end='')  # Reset

    # Código principal
    while True:
        titulo("SISTEMA DE AJUDA PyHelp", 1)  # Título com letras vermelhas
        cmd = input("Função ou biblioteca ('FIM' para encerrar): ").strip()
        if cmd.upper() == 'FIM':
            titulo("ATÉ LOGO!", 1)  # Título de saída em vermelho
            break
        else:
            ajuda(cmd)
            
ex106()

