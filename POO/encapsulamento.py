class Conta:
    def __init__(self, conta, agencia, saldo=0.0):
        self.agencia = agencia
        self.conta = conta
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor
        self.verSaldo()
        self.__mensagem()

    def verSaldo(self):
        print(self.__saldo)

    def __mensagem(self):
        print(f"Bom dia, seu depósito foi feito.")

c1 = Conta(3365, '1234-5')
c1.depositar(200)
c1.verSaldo()

#def main serve pra mostrar todas as func do código

# def main():
#     ver_saldo()
#     depositar()
#     consultar

#para que não funcione simplesmente trocar o valor da variável saldo
#não conseguir por meios normal acessar o saldo, apenas com def

#quebrar o código em várias funções - quebrar sempre em várias funcções
# pq fica melhor de ler etc