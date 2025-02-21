# Exercício 102: Crie um programa que tenha uma função chamada fatorial(), que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não o processo de cálculo do fatorial.
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