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

def leiaFloat(msg):
    while True:
        try:
            f = input(msg).strip().replace(',', '.')
            return float(f)
        except ValueError:
            print('\033[0;31mERRO! Digite um número REAL válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO usuário preferiu não digitar este número.\033[m')
            return 0  # Retorna 0 no caso de interrupção
