def exercicio96 ():

    #Exercício 96: Faça um programa que tenha uma 
    # função chamada área(), que receba as dimensões de um 
    # terreno retangular (largura e comprimento) e 
    # mostre a área do terreno.
    def area(larg, comp):
        tam = larg * comp
        print(f'A area de um terreno {larg} x {comp} é de {tam}m²')

    #Programa Principal
    print('Controle de Terrenos')
    print('-'*30)
    l = float(input('LARGURA(m): '))
    c = float(input('COMPRIMENTO(m): '))
    area(l, c)

def exercicio97 ():
    #Exercício 97: Faça um programa que tenha uma 
    #função chamada escreva(), que receba um texto qualquer como parâmetro
    #e mostre uma mensagem com tamanho adaptável.
    #Exemplo:
    #escreva("Olá, Mundo!"), a saída deve ser:
    #~~~~~~~~~~
    #Ola, Mundo
    #~~~~~~~~~~
    def escreva(txt):
        tam = len(txt) + 4
        print('~'*tam)
        print(f'{txt}'.center(tam))
        print('~'*tam)

    #Codigo principal
    escreva('Oi meu chapa')
    escreva('Gustavo')
    escreva('oi')

def exercicio98 ():
    #Exercício 98: Faça um programa que tenha uma função chamada contador(), 
    # que receba três parâmetros: início, fim e passo, e realize a contagem.
    #Seu programa tem que realizar três contagens através da função criada:
    #   De 1 até 10, de 1 em 1.
    #   De 10 até 0, de 2 em 2.
    #   Uma contagem personalizada.
    from time import sleep

    def contador(inicio, fim, passo):
        if passo == 0:
            passo = 1

        if inicio > fim and passo > 0:
            passo = -passo
            
        for i in range(inicio, fim + (1 if passo > 0 else -1), passo):
            print(i ,end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
        print('-=-'*10)

    #Codigo principal
    print('-=-'*10)
    print('Contagem de 1 até 10 de 1 em 1')
    contador(inicio=1, fim=10, passo=1)

    print('Contagem de 10 até 0 de 2 em 2')
    contador(inicio=10, fim=0, passo=2)

    print('Agora é sua vez')
    i = int(input('INICIO: '))
    f = int(input('FIM: '))
    p = int(input('PASSO: '))
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    contador(i, f, p)

def exercicio99 ():
    #Exercício 99: Faça um programa que tenha uma função chamada maior(), 
    # que receba vários parâmetros com valores inteiros. Seu programa 
    # tem que analisar todos os valores e dizer qual deles é o maior.
    from random import randint
    from time import sleep

    def maior(*num):

        print('Analisando os valores passados...')
        if len(num) > 0:
            for i in num:
                print(i, end=" ", flush=True)
                sleep(.5)
            print(f'Foram informados {len(num)} valores ao todo')
            print(f'O maior numero foi: {max(num)}')
            print('-=-'*10)
            
        else:
            print('Não foram informados valores')
            print('Maior valor foi 0')

    #Codigo principal
    maior(randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
    maior(randint(1,10), randint(1,10), randint(1,10))
    maior(randint(1,10), randint(1,10))
    maior(randint(1,10))
    maior()

def exercicio100 ():
    #Exercício 100: Faça um programa que tenha uma lista chamada números 
    #e duas funções chamadas sorteia() e somaPar().
    #   A primeira função vai sortear 5 números e colocá-los dentro da lista.
    #   A segunda função vai mostrar a soma entre todos os valores pares 
    #sorteados pela função anterior.
    from random import randint
    from time import sleep

    def sorteia(lista):
        print('Sortedo 5 valores: ',end='')
        for i in range(0, 5):
            num = randint(0, 10)
            numeros.append(num)
            print(num, end=' ', flush=True)
            sleep(.5)
        print()

    def somaPar(lista):
        s = 0
        for num in numeros:
            if num % 2 == 0:
                s += num
        print(f'A soma dos pares entre {numeros}: {s}')


    #Codigo principal
    numeros = []
    sorteia(numeros)
    somaPar(numeros)

exercicio100()