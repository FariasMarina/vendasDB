from abc import ABC, abstractmethod
import arrow


class Conta(ABC):
    def __init__(self, agencia, numero, nome, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.nome = nome
        self.__saldo = saldo

    def exibir_saldo(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        self.__saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass


class Conta_corrente(Conta):
    def __init__(self, agencia, numero, nome, saldo, limite=200):
        super().__init__(agencia, numero, nome, saldo=0)
        self.__saldo = saldo
        self.__limite = limite


    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo}')


    def sacar(self, valor):
        if valor > (self.__saldo + self.__limite):
            print('Saldo insuficiente')
        else:
            valor -= self.__saldo
            print('Saque realizado')

            self.exibir_saldo()


class Conta_poupanca(Conta):
    def __init__(self, agencia, numero, nome, saldo=0):
        super().__init__(agencia, numero, nome, saldo=0)
        self.saldo = saldo

    def exibir_saldo(self):
        print(f'{self.nome}, o seu saldo é de {self.__saldo}')

    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente')
        else:
            self.__saldo -= valor
            print('Saque realizado')

            self.exibir_saldo()


