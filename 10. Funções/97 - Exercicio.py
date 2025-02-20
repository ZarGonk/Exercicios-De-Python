#Exercício 97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
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
