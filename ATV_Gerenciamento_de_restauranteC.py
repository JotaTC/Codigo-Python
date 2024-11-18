class ItemMenu:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def __str__(self):
        return f"Nome: {self.nome}\nPreço: {self.preco}"

class PratoPrincipal(ItemMenu):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return super().__str__() + f"\nDescrição: {self.descricao}"

class Sobremesa(ItemMenu):
    def __init__(self, nome, preco, tipo):
        super().__init__(nome, preco)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f"\nTipo: {self.tipo}"

class Restaurante():
    def __init__(self):
        self.menu = []

    def adicionar_item_menu(self,itens):
        self.menu.append(itens)

    def listar(self):
        cont = 0
        for cardapio in self.menu:
            cont += 1
            print(f"{cont}: Comida")
            print(cardapio.__str__())
            print( )
