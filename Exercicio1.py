class Pessoa:
    
    def __init__(self, nome, endereco, valorPagamento, contatos):
        self.nome = nome
        self.endereco = endereco
        self.valorPagamento = valorPagamento
        self.contatos=contatos
        
    
class PessoaFisica(Pessoa):
    def __init__(self, cpf, nome, endereco, valorPagamento: float, contatos ):
        super().__init__(nome, endereco, valorPagamento, contatos)
        self.cpf = cpf
        self.imposto = 0.9
    
    def realizarPagamento(self):
        return self.valorPagamento  * self.imposto
    
    
class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nomeFantasia, razaoSocial, imposto, endereco, valorPagamento, contatos):
        super().__init__(nome, endereco, valorPagamento, contatos)
        self.cnpj = cnpj
        self.nomeFantasia = nomeFantasia
        self.razaoSocial = razaoSocial
        self.imposto = 0.8
        
    def realizarPagamento():
        self.valorPagamento = valorPagamento * imposto



pessoa = Pessoa('Victor',"Dom Pedro II", 100,["1","2","3"])
pessoaF = PessoaFisica ('33676876857','Victor',"Dom Pedro II", 100,["1","2","3"])
print(pessoaF.realizarPagamento)    