from random import randint


class Personagem:
    def __init__(self, full_name, life, level) -> None:
        self.__full_name = full_name
        self.__life = life
        self.__level = level

    def get_name(self):
        return self.__full_name

    def get_life(self):
        return self.__life

    def get_level(self):
        return self.__level

    def show_details(self):
        return f"Nome: {self.get_name()}\nvide: {self.get_life()} \nNivel: {self.get_level()}"

    def receive_damage(self, damage):
        self.__life -= damage
        if self.__life < 0:
            self.__life = 0

    def __calculate_damage(self):
        return randint(self.get_level() * 2, self.get_level() * 4)

    def atack(self, target):
        damage = self.__calculate_damage()
        target.receive_damage(damage)
        print(
            f"\n{self.get_name()} atacou o {target.get_name()} e causou {damage} dano"
        )
