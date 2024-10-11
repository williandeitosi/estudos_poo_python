import os

from personagens.heroi import Heroi
from personagens.vilao import Vilao


class Jogo:
    def __init__(self) -> None:
        self.heroi = Heroi(full_name="Batman", life=100, level=5, skill="hadouken")
        self.vilao = Vilao(full_name="Homem de fogo", level=3, life=50, tipo="Voador")

    def iniciar_batalha(self):
        print("\nINCIANDO BATALHA\n")
        while self.heroi.get_life() > 0 and self.vilao.get_life() > 0:
            print("\nDetalhes dos Personagens:\n")
            print(self.heroi.show_details(), "\n")
            print(self.vilao.show_details(), "\n")

            input("Pressione <Enter> para atacar...")
            choice = input("Escolha (1 - ataque basico, 2 - super): ")
            os.system("cls" if os.name == "nt" else "clear")

            if choice == "1":
                self.heroi.atack(self.vilao)
            if choice == "2":
                self.heroi.superATK(self.vilao)
            if choice not in ["1", "2"]:
                print("escolha invalida tente novamente !")

            if self.vilao.get_life() > 0:
                self.vilao.atack(self.heroi)

        if self.heroi.get_life() > 0:
            print(f"Parabens o {self.heroi.get_name()} VENCEU!")
        else:
            print("Você PERDEU esta batalha")


iniciar = Jogo()
iniciar.iniciar_batalha()
