class Produto:
    def __init__(self, nomeloja, preco, descricao="Produto de informática"):
        self.__nomeloja = nomeloja
        self.__preco = preco
        self.__descricao = descricao

    @property
    def nomeloja(self):
        return self.__nomeloja

    @nomeloja.setter
    def nomeloja(self, nomeloja):
        self.__nomeloja = nomeloja

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao
        
    def getDescricao(self):
        return self.__descricao
        
class Mouse(Produto):
    def __init__(self, nomeloja, preco, tipo, descricao="Produto de informática"):
        super().__init__(nomeloja, preco, descricao)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo
    
    def getDescricao(self):
        return f"{super().getDescricao()}\nTipo: {self.tipo}"
    
    def __repr__(self):
        return f'Mouse({super().nomeloja}, {super().preco}, {self.tipo})'


class Livro(Produto):
    def __init__(self, nomeloja, preco, autor, descricao="Produto de informática"):
        super().__init__(nomeloja, preco, descricao)
        self.__autor = autor


    @property
    def autor(self):
        return self.__autor
    
    def getDescricao(self):
        return f"{super().getDescricao()}\nAutor: {self.autor}"

    def __repr__(self):
        return f'Livro({super().nomeloja}, {super().preco}, {self.autor})'

def main():
    carrinho = []

    # Adicionando mouses ao carrinho
    mouse1 = Mouse("Loja A", 20.0, "Óptico, Saída USB. 1.600 dpi")
    mouse2 = Mouse("Loja B", 25.0, "Bluetooth, Sem fio. 2.000 dpi")

    carrinho.append(mouse1)
    carrinho.append(mouse2)

    # Adicionando livros ao carrinho
    livro1 = Livro("Loja C", 30.0, "Autor X", "Livro de Ficção")
    livro2 = Livro("Loja D", 35.0, "Autor Y", "Livro des Não Ficção")

    carrinho.append(livro1)
    carrinho.append(livro2)

    # Exibindo as descrições dos produtos no carrinho
    for produto in carrinho:
        print(f"\n{produto} ")

if __name__ == "__main__":
    main()