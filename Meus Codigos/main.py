from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, name, nick):
        self.name = name
        self.nick = nick
        self.games = []
    
    def add_favorite(self, name_game):
        self.games.append(name_game)
        self.games.sort()

    def card(self):
        jogos_formatados = "\n".join(f"[green]- {game}[/]" for game in self.games)

        conteudo = (
            f"[bold]Nome Real:[/] [white on red]{self.name}[/]\n\n"
            f"[bold]Jogos Favoritos:[/]\n{jogos_formatados}"
        )

        game_sheet = Panel(
            conteudo,
            title=f"[cyan]Jogador <{self.nick}>[/]",
            border_style="blue"
        )

        print(game_sheet)

g1 = Gamer('Gustavo', 'ZarGonk')

g1.add_favorite('Terraria')
g1.add_favorite('Ark Survivel Evolved')
g1.add_favorite('Fallout New Vegas')
g1.add_favorite('Sniper Elite')

g1.card()