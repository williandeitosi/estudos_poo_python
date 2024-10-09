class Fila:
    fila = []

    def entrar(self, full_name):
        self.fila.append(full_name)


supermercado = Fila()

supermercado.entrar("willian")

supermercado.entrar("Rafaela")
supermercado.entrar("John")
print(supermercado.fila)
