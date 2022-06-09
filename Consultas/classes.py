from abc import abstractmethod , ABC

class Venda:
    def __init__(self , codImovel , mesVenda , anoVenda , valorVenda):
        self.__codImo = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valor = valorVenda

    def getCod(self):
        return self.__codImo

    def getMesVenda(self):
        return self.__mesVenda

    def getAnoVenda(self):
        return self.__anoVenda
    
    def getValor(self):
        return self.__valor

class Vendedor(ABC):
    def __init__(self , codigo , nome ):
        self.__cod = codigo 
        self.__nome = nome

        self.__ven = []

    def getCodigo(self):
        return self.__cod
    def getNome(self):
        return self.__nome
    def getVendas(self):
        return self.__ven

    def adicionaVenda(self , pCodImovel , pMes , pAno , pValor):
        newVenda = Venda(pCodImovel , pMes , pAno , pValor)
        self.__ven.append(newVenda)
    
    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self , pMes , pAno):
        pass



class Contratado(Vendedor):
    def __init__(self, codigo, nome ,salFixo, nrCartTrabalho):
        super().__init__(codigo, nome)
        self.__nroCartTrabalho = nrCartTrabalho
        self.__salFixo = salFixo

    def getNroCartTrabalho(self):
        return self.__nroCartTrabalho

    def getSalFixo(self):
        return self.__salFixo
    
    def getDados(self):
        return 'Nome: {} - Nro Carteira de Trabalho: {}'.format(self.getNome() , self.getNroCartTrabalho())

    def calculaRenda(self, pMes, pAno):
        vendas = self.getVendas()
        comissao = 0
        for each in vendas:
            if pMes == each.getMesVenda() and pAno == each.getAnoVenda():
                comissao += each.getValor()/100
        rendaTotal = self.__salFixo + comissao
        return rendaTotal


class Comissionado(Vendedor):
    def __init__(self, codigo, nome , cpf , comissao):
        super().__init__(codigo, nome)
        self.__cpf = cpf
        self.__comis = comissao

    def getCpf(self):
        return self.__cpf
    
    def getComissao(self):
        return self.__comis

    def getDados(self):
        return 'Nome : {} - Nro Cpf: {}'.format(self.getNome() , self.getCpf() )

    def calculaRenda(self, pMes, pAno):
        vendas = self.getVendas()
        rendaTot = 0
        for each in vendas:
            if pMes == each.getMesVenda() and pAno == each.getAnoVenda():
                rendaTot += (each.getValor()/100) * self.getComissao()
        return rendaTot
    
    


if __name__ == "__main__":
    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = {funcContratado, funcComissionado}
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))