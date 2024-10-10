# Herança multipla


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def emitir_som(self): ...


class Mamifero(Animal):
    def amamentar(self):
        return f"{self.name} está amamentando"


class Ave(Animal):
    def voar(self):
        return f"{self.name} está voando"


class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return f"Morcego esta emitindo som"


batman = Morcego("Batman")
# metodo da class Animal
print(batman.name)
print(batman.emitir_som())
# metodo da class amamentar
print(batman.amamentar())
# metodo da class Ave
print(batman.voar())
