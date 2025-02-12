# Exercício 89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

boletim = []
while True:
    nome = str(input('Enter the name: '))
    n1 = float(input('Enter the first note: '))
    n2 = float(input('Enter the second note: '))

    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])

    # Pergunta se quer continuar, caso contrário, para
    stop = ''
    while stop not in ('Y', 'N'):
        stop = str(input('Want to stop [Y/N]: ')).strip().upper()
        if stop == 'N':
            break
    if stop == 'Y':
        break

# Exibindo o boletim com a média de cada aluno
print('\n')
print(f"{'BOLETIM':=^30}")
print(f"{'N°.':<4} {'Nome':<15} {'Média':>7}")
print('-=' * 15)
for i, a in enumerate(boletim):
    print(f'{i + 1:<4} {a[0]:<15} {a[2]:>7.2f}')

# Mostra as notas de um aluno específico
while True:
    opcao = int(input('Do you want to see which student\'s grade (999 stops): '))
    if opcao == 999:
        print("Finalizando...")
        break
    if 0 <= opcao - 1 < len(boletim):
        print(f'Notas de {boletim[opcao - 1][0]} são {boletim[opcao - 1][1]}')
    else:
        print("Aluno não encontrado.")