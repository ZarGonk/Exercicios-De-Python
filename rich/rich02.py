from rich import print
from rich.table import Table


table = Table(title="Tabela de preços")

table.add_column('Name', style="green")
table.add_column('Price', justify='center', style='red')

table.add_row('Lápis', 'R$ 1,50')
table.add_row('Borracha', 'R$ 5,00')


print(table)