class Pizza:
    pedacos = 8

    def mudar_tamanho(cls, tamanho):
        cls.pedacos = tamanho
        print(f"O tamnho da pizza agora é {cls.pedacos} pedaços ")

    @staticmethod
    def ingredientes():
        return "Massa"


class Musarela(Pizza):
    sabor = "Musarela"

    def exibri(self):
        print(f"sabor {self.sabor}")
        print(f"pedacos {self.pedacos}")

    @staticmethod
    def ingredientes():
        return ["Queijo", "tomate", "azeitona"]


class Calabresa(Pizza):
    sabor = "Calabresa"

    def exibri(self):
        print(f"sabor {self.sabor}")
        print(f"pedacos {self.pedacos}")


class MeioAMeio(Calabresa, Musarela):
    def exibir(self):
        print(f"meio {Musarela.sabor}, meio {Calabresa.sabor}")


mus = Musarela()
mus.exibri()

cal = Calabresa()
cal.exibri()


meio = MeioAMeio()
meio.exibir()
