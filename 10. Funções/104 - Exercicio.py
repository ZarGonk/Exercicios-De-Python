# Exercício 104: Crie um programa que tenha a 
# função chamada leiaInt(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
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
