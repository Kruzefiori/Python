from abc import ABC 
from datetime import date


class Conta:
    def __init__(self , nroConta , nome , limite, senha):
        self.__nroConta = nroConta
        self.__nome = nome
        self.__senha = senha
        self.__saldo = limite
        self.__limite = limite
        self.__tran = []

#--------------------------------GETTERS-------------------------#
    def getnroConta(self):
        return self.__nroConta
        
    def getNome(self):
        return self.__nome

    def getSenha(self):
        return self.__senha

    def getSaldo(self):
        return self.__saldo

    def getLimite(self):
        return self.__limite
        
    def getTransacoes(self):
        return self.__tran

#-----------------------FUNÇÔES-----------------------------------#

    def adicionaDeposito(self, valor, data , nomeDepositante):
        self.__saldo += valor
        newDep = Deposito(valor ,  data , nomeDepositante)
        self.getTransacoes().append(newDep)

    def adicionaSaque(self,valor ,  data, senha):
        if senha != self.getSenha() or valor > self.getSaldo():return False
        else:
            newSaque = Saque(valor ,  data, senha)
            self.__saldo = self.__saldo - valor
            self.getTransacoes().append(newSaque)
            return True

    def adicionaTransf(self,valor , data, senha, contaFavorecida):
        if senha != self.getSenha() or valor > self.getSaldo():return False
        else:
            newTrans = Transferencia(valor , data, senha, contaFavorecida)
            self.__saldo = self.__saldo - valor
            contaFavorecida.__saldo += valor
            contaFavorecida.__limite += valor
            self.getTransacoes().append(newTrans)
            return True

    def calculaSaldo(self):
        tra = self.getTransacoes()
        saldoRetorno = self.getLimite()
        for each in tra:
            if type(each).__name__ == 'Deposito':
                saldoRetorno = saldoRetorno + each.getValor()
            if type(each).__name__ == 'Saque':
                saldoRetorno =  saldoRetorno - each.getValor()
            if type(each).__name__ == 'Transferencia':
                saldoRetorno =  saldoRetorno - each.getValor()
        return saldoRetorno
            
class Transacao(ABC):
    def __init__(self , valor , data):
        self.__valor = valor
        self.__data = data

    def getValor(self):
        return self.__valor

    def getData(self):
        return self.__data
    
class Saque(Transacao):
    def __init__(self, valor, data , senha):
        super().__init__(valor, data)
        self.__senha = senha

    def getSenha(self):
        return self.__senha

class Transferencia(Transacao):
    def __init__(self, valor, data , senha , contaFav):
        super().__init__(valor, data)
        self.__senha = senha
        self.__contaFav = contaFav
    
    def getSenha(self):
        return self.__senha

    def getContaFav(self):
        return self.__contaFav

class Deposito(Transacao):
    def __init__(self, valor, data, nomeDepositante):
        super().__init__(valor, data)
        self.__nomeDepositante = nomeDepositante

    def getNomeDepositante(self):
        return self.__nomeDepositante

if __name__ == "__main__":
    c1 = Conta(1234, 'Jose da Silva', 1000, 'senha1')
    c1.adicionaDeposito(5000, date.today(), 'Antonio Maia')
    if c1.adicionaSaque(2000, date.today(), 'senha1') == False:
        print('Não foi possível realizar o saque no valor de 2000')
    if c1.adicionaSaque(1000, date.today(), 'senha-errada') == False:  # deve falhar
        print('Não foi possível realizar o saque no valor de 1000')

    c2 = Conta(4321, 'Joao Souza', 1000, 'senha2')
    c2.adicionaDeposito(3000, date.today(), 'Maria da Cruz')
    if c2.adicionaSaque(1500, date.today(), 'senha2') == False:
        print('Não foi possível realizar o saque no valor de 1500')
    if c2.adicionaTransf(5000, date.today(), 'senha2', c1) == False:  # deve falhar
        print('Não foi possível realizar a transf no valor de 5000')
    if c2.adicionaTransf(800, date.today(), 'senha2', c1) == False:
        print('Não foi possível realizar a transf no valor de 800')
    print('--------')
    print('Saldo de c1: {}'.format(c1.calculaSaldo()))  # deve imprimir 4800
    print('Saldo de c2: {}'.format(c2.calculaSaldo()))  # deve imprimir 1700
