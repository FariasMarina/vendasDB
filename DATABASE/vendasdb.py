import requests
import arrow
from pycpfcnpj import cpf
import sqlite3

conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()

#TODO: Editar prod, editar cliente (CEP), classe Vendas, ranking de vendas e de clientes.

class Cliente:
    def __init__(self, nome, cpfa, cep, cidade, estado, rua):
        self.nome = nome
        self.cpfa = cpfa
        self.cep = cep
        self.cidade = cidade
        self.estado = estado
        self.rua = rua

    def cadastrarCliente(self):

        if self.validarCep() and self.validarCPF():
            cursor.execute(f'INSERT INTO clientes(nome_cliente, cpf_cliente, cep_cliente, cidade_cliente, '
                           f'estado_cliente,rua_cliente)'
                           f'VALUES("{self.nome}", "{self.cpfa}", "{self.cep}", "{self.cidade}", "{self.estado}", "{self.rua}")')
            print(f'O(A)cliente {self.nome} foi cadastrado(a) com sucesso.')
        elif not self.validarCPF():
            print('O CPF é inválido, tente novamente.')
        elif not self.validarCep():
            print('O CEP é inválido, tente novamente.')
        else:
            print('CPF e CEP inválidos, revise as informações.')

    def validarCep(self):
        try:
            cep = self.cep
            arq = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
            self.cidade = arq.json()['localidade']
            self.estado = arq.json()['uf']
            self.rua = arq.json()['logradouro']
            return True
        except:
            print('Cep Inválido')
            return False

    def validarCPF(self):
        try:
            cpf.validate(self.cpfa)
            return True
        except:
            return False

    def alterarCliente(self, cpfa):
        choices = {1: 'cpf_cliente', 2: 'nome_cliente', 3:'cep_cliente', 4:'rua_cliente', 5:'cidade_cliente',
                   6: 'estado_cliente'}
        choice = int(input(f'{30*"≡"}\nDigite o que deseja alterar:\n\n[1] CPF - [2] NOME - [3] CEP\n[4] RUA - [5] CIDADE - '
                       f'[6] ESTADO\n{20*"⋯"}\nDigite: '))
        print(f'{30 * "≡"}\n')
        answer = input(f'Digite a nova resposta: ')

        print(choices[choice])

        # if choice == 3:
        #     choice = self.cep
        #     choice.validarCep()
        # elif choice == 1:
        #     self.validarCPF()
        # else:
        #     pass

        cursor.execute(f'UPDATE clientes SET {choices[choice]}="{answer}" WHERE cpf_cliente={cpfa}')
        print(f'Alteração feita com sucesso.')

    def excluirCliente(self, cpfa):
        certeza = input('Tem certeza?(S/N): ').upper()
        if certeza == 'S':
            cursor.execute(f'DELETE FROM clientes WHERE cpf_cliente="{cpfa}"')
            print(f'O registro do cliente {self.nome} foi excluído.')
        else:
            print('O registro não foi excluído.')

    def rankearClientes(self):
        pass


class Produtos:
    def __init__(self, nome, cod_barras, fabricante):
        self.cod_barras = cod_barras
        self.nome = nome
        self.fabricante = fabricante

    def cadastrarProduto(self):
        try:
            cursor.execute(f'INSERT INTO produtos(cod_barras, nome_produto, fabricante_produto)'
                           f'VALUES (?, ?, ?)', (self.cod_barras, self.nome, self.fabricante))
            print(f'Produto {self.nome} cadastrado com sucesso.')
        except:
            print('Ops, algo deu errado ao cadastrar o produto. Verifique se já não foi criado.')

        conexao.commit()

    def editarProduto(self):
        id_prod = int(input('Digite o id do produto que quer alterar: '))
        choices = {1: 'nome_produto', 2: 'fabricante_produto', 3: 'cod_barras'}
        choice = int(input('O que você deseja editar? [1] Nome [2] Fabricante [3] Código de barras'))
        answer = input('Digite a alteração: ')

        cursor.execute(f'UPDATE clientes SET {choice}="{answer}" WHERE id_produto={id_prod}')
        print(f'Alteração feita com sucesso.')

    def excluirProduto(self, id):
        certeza = input('Tem certeza?(S/N): ').upper()
        if certeza == 'S':
            cursor.execute(f'DELETE FROM produtos WHERE id_produto="{id}"')
        print(f'O produto {self.nome} foi excluído.')


class Venda:
    def __init__(self, data, hora, cpfa, cod_barras, qtde, valor_un, valor_tt):
        self.data = data
        self.hora = hora
        self.cpfa = cpfa
        self.cod_barras = cod_barras
        self.qtde = qtde
        self.valor_un = valor_un
        self.valor_tt = valor_tt

    def novaVenda(self):
        venda = input('Digite o produto qe qur vender pelo id: ')
        cursor.execute(f'INSERT INTO produtos(data_venda, hora_venda, cpf_cliente, cod_barras, quantidade, '
                       f'valor_unitario, valor_total)'
                       f'VALUES (?, ?, ?, ?, ?, ?, ?)', (self.data, self.hora, self.cod_barras, self.qtde,
                                                         self.valor_un, self.valor_tt))
        print(f'Venda concluída com sucesso.')

    def alterarVenda(self):
        pass

    def excluirVenda(self, cpfa, cod_barras):
        certeza = input('Tem certeza?(S/N): ').upper()
        if certeza == 'S':
            cursor.execute(f'DELETE FROM vendas WHERE cpf_cliente="{cpfa}" and cod_barras="{cod_barras}"')
        print(f'A venda do produto {cod_barras} foi excluída.')



marina = Cliente('Marina', '46007798003', '89030353', 'Rio', 'Rio', 'Rio')
# marina.validarCPF() OK----------------------
# marina.validarCep() #OK----------------------
# marina.endereco()   OK----------------------
# marina.cadastrarCliente() OK ---------------
# marina.alterarCliente('46007798003')@@@@@@@@
# marina.excluirCliente('1682526576') OK -----


p1 = Produtos('Suco de uva', '127721', 'Ambev')
# p1.cadastrarProduto() #OK ------------------
# p1.excluirProduto(4) # OK ------------------
# p1.editarProduto() # @@@@@@@@@@@@@@@@@@@@@@@

v1 = Venda()
conexao.commit()
cursor.close()
conexao.close()


# data, hora, cpfa, cod_barras, qtde, valor_un, valor_tt):
#         self.data = data
#         self.hora = hora
#         self.cpfa = cpfa
#         self.cod_barras = cod_barras
#         self.qtde = qtde
#         self.valor_un = valor_un
#         self.valor_tt = valor_tt
