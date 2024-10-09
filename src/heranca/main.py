class Animal:
    def __init__(self, full_name: str) -> None:
        self.full_name = full_name

    def apresentacao(self):
        return f"Olá, meu nome é {self.full_name}"

    def barulho(self): ...


class Cachorro(Animal):
    def barulho(self):
        return f"AU AU"


rex = Cachorro("Rex")
res = rex.apresentacao()
barulho = rex.barulho()
print(res)
print(barulho)
