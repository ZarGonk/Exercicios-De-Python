def ex1():
    #Exercício 1: Implemente uma função que receba uma lista de números e imprima a soma de todos os elementos da lista.
    def lista(numeros):
        soma = sum(numeros)
        print(f'A soma de {numeros} é {soma}')

    numeros = [1, 4, 1]
    lista(numeros)

def ex2():
    #Exercício 2: Crie uma função que receba um número inteiro e imprima o fatorial desse número.
    def fatorial(num):
        fat = 1
        for i in range(num, 1, -1):
            fat = i * fat
        print(f'O fatorial de {num} é {fat}')

    #Codigo principal
    fatorial(int(input('Digite o numero que deseja o fatorial: ')))

def ex3():
    #Exercício 3: Escreva uma função que receba uma string e imprima a string invertida.
    def txt(msg):
        inversa = msg[::-1]
        print(inversa)


    #Codigo Principal
    string = str(input('Digite seu texto: ')).strip().lower().replace(' ','')
    txt(string)

def ex4():
    #Exercício 4: Desenvolva uma função que receba uma lista de números e imprima a média dos elementos da lista.
    def lista(numeros):
        media = sum(numeros) / len(numeros)
        print(media)

    #Codigo principal
    numeros = [10, 10, 7]
    lista(numeros)

def ex5():
    #Exercício 5: Implemente uma função que receba uma lista de números e imprima todos os números pares da lista.
    def pares(lista):
        soma = 0
        for i in lista:
            if i % 2 == 0:
                soma += i
        print(f'A soma dos pares de {lista} é {soma}')

    numeros = [1, 4, 2, 3]
    pares(numeros)

def ex6():
    #Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos através de uma função. Seu script também deve fornecer a média dos três números, através de uma segunda função que chama a primeira.
    # Função invocando função
    def soma(a=0, b=0, c=0):
        return a + b + c
    
    def media(total):
        return total / 3
    
    a = int(input('Valor 1: '))
    b = int(input('Valor 2: '))
    c = int(input('Valor 3: '))

    resultado = soma(a, b, c)
    média = media(resultado)

    print(f'A soma de {a}, {b} e {c}: {resultado}')
    print(f'Media é {média}')

def ex7():
    #Faça um programa que recebe três números do usuário, e identifica o maior através de uma função e o menor número através de outra função.

    def maior(a, b, c):
        numeros = list()
        numeros.append(a)
        numeros.append(b)
        numeros.append(c)
        return max(numeros)
    
    def menor(a, b, c):
        numeros = list()
        numeros.append(a)
        numeros.append(b)
        numeros.append(c)
        return min(numeros)
    
        
    def menu():
        a = int(input('Valor 1: '))
        b = int(input('Valor 1: '))
        c = int(input('Valor 1: '))

        print('~'*20)
        print('Maior: ',maior(a, b, c))
        print('Menor: ',menor(a, b, c))
        print('~'*20)

    while True:
        menu()

def ex8():
    #Crie uma função que recebe um inteiro positivo e teste para saber se ele é primo ou não. Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.

    def primo(num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def exibe():
        num = int(input('Enter the number: '))
        for i in range(2, num+1):
            if primo(i):
                print(i, end=' -> ')
  
        print('FIM')

    exibe()

ex8()