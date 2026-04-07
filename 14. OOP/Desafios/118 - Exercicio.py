from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, title_churras, number_of_people):
        self.title_churras      = title_churras
        self.number_of_people   = number_of_people

    def analisar(self):
        # CONSIDERE:
        # Consumo padrão: 400 g por pessoa
        # Preço: R$82,40/Kg
        meat = 0.4 * self.number_of_people
        tot_value = 82.40 * meat
        value_each_participant = tot_value / self.number_of_people
        conteudo = (
            f"Analisando [green]{self.title_churras}[/] com [blue]{self.number_of_people}[/] convidados\n"
            f"Cada Participante comerá 0.4KG e cada Kg custa [red]R$82.40[/]\n"
            f"Recomendo [blue]comprar {meat:.2f} Kg[/] de carne\n"
            f"O custo total será de [green]R$ {tot_value:,.2f}\n[/]"
            f"Cada Pessoa parará [yellow]R$ {value_each_participant:,.2f}[/] para participante"
        )

        painel = Panel(conteudo, title=self.title_churras)

        print(painel)


c1 = Churrasco('Churras dos Guri', 5)
c1.analisar()
