class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        self.valor = valor
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        if valor > 0 and valor > self.__saldo:
            print(f"Valor: {self.valor} para saque invalido")
        if valor <= 0:
            print("Não é possivel sacar valor negativo ou 0")

    def ver_saldo(self):
        return self.__saldo


conta_willian = ContaBancaria(2000)
print(f"Meu saldo bancário é: R${conta_willian.ver_saldo()}")
conta_willian.depositar(300)
print(f"Meu saldo bancário é: R${conta_willian.ver_saldo()}")
conta_willian.sacar(5000)
print(f"Meu saldo bancário é: R${conta_willian.ver_saldo()}")
