import sqlite3
from abc import ABC, abstractmethod
import arrow
#validar cep, validar cpf

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

class cliente:
    def __init__(self, nome, cpf, cep):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep

    @abstractmethod
    def cadastrar(self):
        cursor.execute(f'INSERT INTO clientes(nome_cliente, cpf_cliente, cep_cliente)'
                       f'VALUES("{self.nome}", "{self.cpf}", "{self.cep}")')
        print(f'O/A cliente {self.nome} foi cadastrado com sucesso.')

# class produto:
#     def __init__(self, id_produto, cod_barras, nome_produto, fac):

class venda:
    pass

marina = cliente('Marina', '123', '234')

marina.cadastrar()