class Pizza:
    pedacos = 8

    def __init__(self, sabor):
        self.sabor = sabor
        print(self.sabor)

    def acabou(self):
        print("Acabou os pedaços...")

    def pegar_pedaco(self):
        if self.pedacos > 0:
            self.pedacos -= 1
            print(f"peguei um pedaço agora restou {self.pedacos}")
            if self.pedacos == 0:
                self.acabou()
        else:
            print("Não há mais pedaços")

    @classmethod
    def mudar_tamanho(cls, pedacos):
        cls.pedacos = pedacos
        print(cls.pedacos)


will = Pizza("Mussarela")

print(will.pedacos)
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
will.pegar_pedaco()
Pizza.mudar_tamanho(10)
will.pegar_pedaco()
will.mudar_tamanho(10)
print(will.pedacos)
rafa = Pizza("Calabresa")
print(rafa.pedacos)
