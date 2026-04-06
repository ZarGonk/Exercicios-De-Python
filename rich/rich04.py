## Exemplo Prático (Mini Sistema)

from rich import print
from rich.table import Table
from rich.panel import Panel

print(Panel("[bold green]Sistema Bancário[/]", subtitle="ZarGonk"))

usuarios = [
    {"id": 1, "nome": "ZarGonk", "saldo": 1000},
    {"id": 2, "nome": "Ana", "saldo": 2500}
]

tabela = Table(title="Clientes")

tabela.add_column("ID", justify="center", style="cyan")
tabela.add_column("Nome", style="magenta")
tabela.add_column("Saldo", justify="right", style="green")

for u in usuarios:
    tabela.add_row(str(u["id"]), u["nome"], f'R$ {u["saldo"]}')

print(tabela)
print("[bold green]✔ Sistema carregado com sucesso![/]")