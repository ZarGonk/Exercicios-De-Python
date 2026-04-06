from rich import print
from rich.panel import Panel


painel = Panel("Painel 1 de exemplo")

painel_com_titulo = Panel("[white] Esta é a mensagem[/]", title='Message', style="red", height=5, width=30)

print(painel)

print(painel_com_titulo)