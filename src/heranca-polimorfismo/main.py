class Animal:
    def __init__(self, full_name: str) -> None:
        self.full_name = full_name

    def apresentacao(self):
        return f"Olá, meu nome é {self.full_name}"

    def barulho(self) -> str:
        return "som generico de animal"


# Herança: a classe Cachorro herdou tudo o que vem da classe Animal
# podemos dizer que a Classe Animal serve como molde para as classes Cachorro e Gato
class Cachorro(Animal):
    # Polimorfismo: peguei o methodo do Animal barulho que nao passava nada para o barulho do cachorro que é AU AU
    def barulho(self):
        return "AU AU"


class Gato(Animal):
    def barulho(self):
        return "MIAU!"


rex = Cachorro("Rex")
yummi = Gato("Yummi")

animais = [rex, yummi]

for animal in animais:
    print(f"O {animal.full_name} faz: {animal.barulho()}")
