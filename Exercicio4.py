class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
        print(f"Contato {contato.nome} adicionado com sucesso.")

    def editar_contato(self, nome, novo_telefone):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.telefone = novo_telefone
                print(f"Contato {contato.nome} editado com sucesso.")
                return
        print(f"Contato {nome} não encontrado.")

    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f"Contato {contato.nome} removido com sucesso.")
                return
        print(f"Contato {nome} não encontrado.")

    def buscar_contato(self, chave):
        resultados = []
        for contato in self.contatos:
            if chave.lower() in contato.nome.lower() or chave in contato.telefone:
                resultados.append(contato)
        return resultados

# Exemplo de uso
agenda = Agenda()

contato1 = Contato("João", "123456789")
contato2 = Contato("Maria", "987654321")

agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)

agenda.editar_contato("João", "111111111")
agenda.remover_contato("Maria")

resultados_busca = agenda.buscar_contato("Jo")
print("Resultados da busca:")
for resultado in resultados_busca:
    print(f"Nome: {resultado.nome}, Telefone: {resultado.telefone}")