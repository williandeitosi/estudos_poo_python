# Abstração: eu crio uma classe abstrata = molde
# obrigando ter os mesmo methodos que tem na classe abstrata


from abc import abstractmethod, ABC


class Veiculo(ABC):
    @abstractmethod
    def Ligar(self): ...

    @abstractmethod
    def Desligar(self): ...


class Carro(Veiculo):
    def __init__(self, full_name) -> None:
        self.full_name = full_name

    def Ligar(self):
        return f"Carro : {self.full_name} liga com a Chave"

    def Desligar(self):
        return f"Carro : {self.full_name} desliga com a Chave"


volvo = Carro("Volvo")
print(volvo.Ligar())
print(volvo.Desligar())
