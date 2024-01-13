class Pessoa:
    def __init__(self, nome, endereco, cpf, rg, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
    
    @property
    def nome(self):
        return f'{self.__nome}'
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        
    @property
    def endereco(self):
        return f'{self.__endereco}'
    
    @nome.setter
    def endereco(self, endereco):
        self.__endereco = endereco
        
    @property
    def cpf(self):
        return f'{self.__cpf}'
    
    @nome.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def rg(self):
        return f'{self.__rg}'
    
    @nome.setter
    def rg(self, rg):
        self.__rg = rg
        
        
    @property
    def telefone(self):
        return f'{self.__telefone}'
    
    @nome.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        

class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, cpf, rg, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida

    @property
    def valor_credito(self):
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito
    
    @property
    def valor_divida(self):
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_credito):
        self.__valor_credito = valor_credito

    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida



class Pessoa:
    def __init__(self, nome, endereco, cpf, rg, telefone):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        
    @property   
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, rg):
        self.__rg = rg
        
    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone



class Fornecedor(Pessoa):
    def __init__(self, nome, endereco, cpf, rg, telefone, valor_credito, valor_divida):
        super().__init__(nome, endereco, cpf, rg, telefone)
        self.__valor_credito = valor_credito
        self.__valor_divida = valor_divida

    @property
    def valor_credito(self):
        return self.__valor_credito

    @valor_credito.setter
    def valor_credito(self, valor_credito):
        self.__valor_credito = valor_credito
        
    @property
    def valor_divida(self):
        return self.__valor_divida

    @valor_divida.setter
    def valor_divida(self, valor_divida):
        self.__valor_divida = valor_divida


    def obter_saldo(self):
        return self.__valor_credito - self.__valor_divida


def exibir_menu():
    print("----- Sistema de Gestão de Pessoas (SGP) -----")
    print("1. Cadastrar Fornecedor")
    print("2. Consultar Fornecedor")
    print("3. Sair")
    

if __name__ == "__main__":
    fornecedor = None

    while True:
        exibir_menu()

        try:
            opcao = int(input("Escolha uma opção (1-3): "))

            if opcao == 1:
                # Cadastramento de Fornecedor
                nome = input("Nome: ")
                endereco = input("Endereço: ")
                cpf = input("CPF: ")
                rg = input("RG: ")
                telefone = input("Telefone: ")
                valor_credito = float(input("Valor de Crédito: "))
                valor_divida = float(input("Valor da Dívida: "))

                fornecedor = Fornecedor(nome, endereco, cpf, rg, telefone, valor_credito, valor_divida)
                print("Fornecedor cadastrado com sucesso!")

            elif opcao == 2:
                # Consulta de Fornecedor
                if fornecedor:
                    print("\nInformações do Fornecedor:")
                    print(f"Nome: {fornecedor.get_nome()}")
                    print(f"Endereço: {fornecedor.get_endereco()}")
                    print(f"CPF: {fornecedor.get_cpf()}")
                    print(f"RG: {fornecedor.get_rg()}")
                    print(f"Telefone: {fornecedor.get_telefone()}")
                    print(f"Valor de Crédito: {fornecedor.get_valor_credito()}")
                    print(f"Valor da Dívida: {fornecedor.get_valor_divida()}")
                    print(f"Saldo: {fornecedor.obter_saldo()}")
                else:
                    print("Nenhum fornecedor cadastrado.")

            elif opcao == 3:
                print("Saindo do Sistema de Gestão de Pessoas (SGP).")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")

if __name__ == '__main__':
    fornecedor = Fornecedor()