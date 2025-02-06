# Exercício 73: Crie uma tupla com os 20 primeiros colocados da Tabela do 
#Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#   Apenas os 5 primeiros colocados.
#   Os últimos 4 colocados da tabela.
#   Uma lista com os times em ordem alfabética.
#   Que posição está o time da Chapecoense (ou outro time de sua preferência, conforme a data do exercício).
brasileirao = ("Botafogo", "Palmeiras", "Flamengo", "Bahia", "Cruzeiro", 
               "São Paulo", "Fortaleza", "Athletico-PR", "Bragantino", 
               "Atlético-MG", "Vasco", "Juventude", "Internacional",
               "Criciúma", "Cuiabá", "Vitória", "Corinthians", "Grêmio",
               "Atlético-GO", "Fluminense")

print(f'Os 5 primeiros colocados do brasileirao : {brasileirao[0:5]}')
print(f'\nOs ultimos 4 colocados são: {brasileirao[16:]}')

ordem = sorted(brasileirao)
print(f'\nLista Em Ordem Alfabetica:\n{ordem}')
print(f'\n Posiçao do Internacional: {brasileirao.index('Internacional')+1}')
