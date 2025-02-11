def leiaInt(msg):
    while True:
        try:
            n = input(msg).strip()
            return int(n)
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número INTEIRO válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar este número.\033[m')
            return 0  # Retorna 0 no caso de interrupção


def linha(tam = 30):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc

