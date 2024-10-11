from random import randint

from personagens.personagem import Personagem


class Heroi(Personagem):
    def __init__(self, full_name, life, level, skill) -> None:
        super().__init__(full_name, life, level)
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def show_details(self):
        return f"{super().show_details()}\nHabilidade: {self.get_skill()}"

    def __calculate_damage(self):
        return randint(self.get_level() * 5, self.get_level() * 10)

    def superATK(self, target):
        super_damage = self.__calculate_damage()
        target.receive_damage(super_damage)
        print(
            f"\n{self.get_name()} usou o {self.get_skill().upper()} no {target.get_name()} e causou {super_damage} dano"
        )
