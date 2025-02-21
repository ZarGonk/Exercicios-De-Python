
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
        


