import requests
import arrow
from pycpfcnpj import cpf
import sqlite3


class Cliente:
    def __init__(self, nome, cpf, cep, cidade, estado, rua):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.rua = rua


    def cadastrarCliente(self):
        self.cep.validarCep()
        print(f'O(A) cliente {self.nome} foi cadastrado(a)')

    def validarCep(self):
        try:
            arq = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
            self.cidade = arq.json()['localidade']
            self.estado = arq.json()['uf']
            self.rua = arq.json()['logradouro']
        except:
            print('Cep Inválido')

    def alterarCliente(self):
        print('O arquivo do cliente tal foi alterado')

    def validarCPF(self):
        print(cpf.validate(self.cpf))

    def excluirCliente(self):
        print(f'O registro do cliente {self.nome} foi excluído.')

    def endereco(self):
        print({self.rua}, {self.cidade}, self.estado)


class Produtos:
    def __init__(self, nome, cod_barras, fabricante):
        self.nome = nome
        self.cod_barras = cod_barras
        self.fabricante = fabricante

    def cadastrarProduto(self):
        pass

    def editarProduto(self):
        pass

    def excluirProduto(self):
        print(f'O produto {self.nome} foi excluído.')


class Venda:
    def __init__(self, data, hora, cpf, cod_barras, qtde, valor_un, valor_tt):
        self.data = data
        self.hora = hora
        self.cpf = cpf
        self.cod_barras = cod_barras
        self.qtde = qtde
        self.valor_un = valor_un
        self.valor_tt = valor_tt

    def novaVenda(self):
        print(f'Concluído com sucesso.')

    def alterarVenda(self):
        pass

    def excluirVenda(self):
        pass


marina = Cliente('Marina', '1682526576', '89030353', 'Rio', 'Rio', 'Rio')
# marina.validarCPF() OK----------------------
# marina.validarCep() OK----------------------
# marina.endereco()   OK----------------------
