class MaquinaDeVendas:
    def __init__(self):
        self.estoque = {}
        self.valor_inserido = 0

    def cadastrar_produto(self, nome, preco, quantidade):
        if nome in self.estoque:
            self.estoque[nome]['quantidade'] += quantidade
        else:
            self.estoque[nome] = {'preco': preco, 'quantidade': quantidade}

    def exibir_estoque(self):
        print("Estoque disponível:")
        for produto, info in self.estoque.items():
            print(f"{produto}: R${info['preco']:.2f} - Quantidade: {info['quantidade']} unidades")

    def selecionar_produto(self, nome):
        if nome in self.estoque and self.estoque[nome]['quantidade'] > 0:
            return self.estoque[nome]['preco']
        else:
            return None

    
    def inserir_dinheiro(self, valor):
        self.valor_inserido += valor


    def calcular_troco(self, preco_produto):
        troco = self.valor_inserido - preco_produto
        if troco >= 0:
            return troco
        else:
            return None

    def realizar_compra(self, nome_produto):
        preco_produto = self.selecionar_produto(nome_produto)

        if preco_produto is not None:
            if self.valor_inserido >= preco_produto:
                troco = self.calcular_troco(preco_produto)
                self.estoque[nome_produto]['quantidade'] -= 1
                self.valor_inserido = 0
                return troco
            else:
                return "Dinheiro insuficiente. Por favor, insira mais dinheiro."
        else:
            return "Produto não disponível no estoque."


# Exemplo de uso:
maquina = MaquinaDeVendas()

maquina.cadastrar_produto("Chocolate", 2.50, 5)
maquina.cadastrar_produto("Refrigerante", 3.00, 3)
maquina.cadastrar_produto("Salgadinho", 1.50, 10)

maquina.exibir_estoque()

maquina.inserir_dinheiro(5.00)

produto_selecionado = "Refrigerante"
troco = maquina.realizar_compra(produto_selecionado)

if isinstance(troco, str):
    print(troco)
else:
    print(f"Compra realizada! Troco: R${troco:.2f}")

maquina.exibir_estoque()
