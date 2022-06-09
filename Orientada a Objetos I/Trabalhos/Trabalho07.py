from abc import ABC, abstractmethod
from tkinter import X

class Venda():
    def __init__(self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda

    def getCodImovel(self):
        return self.__codImovel

    def getMesVenda(self):
        return self.__mesVenda

    def getAnoVenda(self):
        return self.__anoVenda
    
    def getValorVenda(self):
        return self.__valorVenda

class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []

    def getCodigo(self):
        return self.__codigo

    def getNome(self):
        return self.__nome

    def getVendas(self):
        return self.__vendas

    def adicionaVenda(self, codigo, mes, ano, valor):
        venda = Venda(codigo, mes, ano, valor)
        return self.__vendas.append(venda)
    
    @abstractmethod
    def getDados(self):
        pass
    
    @abstractmethod
    def calculaRenda(pMes, pAno):
        pass

class Contratado(Vendedor):
    #                   (1001,  'João da Silva',     2000,           1234)
    def __init__(self, codigo,   nome,            salarioFixo , nroCartTrabalho ):
        super().__init__(codigo, nome)
        self.__nroCartTrabalho = nroCartTrabalho
        self.__salarioFixo = salarioFixo

        self.__comissao = 1
        
    def getNroCartTrabalho(self):
        return self.__nroCartTrabalho

    def getSalarioFixo(self):
        return self.__salarioFixo

    def getDados(self):
        return 'Nome: ' + super().getNome() + ' - Nro Carteira: ' + str(self.__nroCartTrabalho)

    def calculaRenda(self, pMes, pAno):
        comissaoMes = 0
        for venda in self.getVendas():
            if venda.getMesVenda() == pMes and venda.getAnoVenda() == pAno:                
                comissaoMes += venda.getValorVenda()/100
        salarioFinal = self.__salarioFixo + comissaoMes                 
        return salarioFinal
        
 
class Comissionado(Vendedor):
    def __init__ (self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao

    def getNroCPF(self):
        return self.__nroCPF

    def getComissao(self):
        return self.__comissao

    def getDados(self):
        return 'Nome: ' + super().getNome() + ' - Nro CPF:' + str(self.__nroCPF)

    def calculaRenda(self, pMes, pAno):
        salarioMes = 0
        for venda in self.getVendas():
            if venda.getMesVenda() == pMes and venda.getAnoVenda() == pAno:                
                salarioMes =+ self.__comissao *  (venda.getValorVenda()/100)        
        return salarioMes        

if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))