from personagens.personagem import Personagem


class Vilao(Personagem):
    def __init__(self, full_name, life, level, tipo) -> None:
        super().__init__(full_name, life, level)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def show_details(self):
        return f"{super().show_details()}\ntipo: {self.get_tipo()}"
