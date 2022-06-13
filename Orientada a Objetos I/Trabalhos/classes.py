from abc import ABC , abstractmethod
class Disciplina:
    def __init__(self, cod, nome, ch, optativa) -> None:
        self.__cod = cod
        self.__name = nome
        self.__ch = ch
        self.__op = optativa


    def getCod(self):
        return self.__cod

    def getName(self):
        return self.__name

    def getCh(self):
        return self.__ch

    def getOp(self):
        if self.__op == False:
            return False
        else:
            return True

class Grade:
    def __init__(self, nome) -> None:
        self.__name = nome

        self.__mats = []

    def getName(self):
        return self.__name

    def getMateria(self):
        return self.__mats

    def addMateria(self, cod, nome, ch, optativa):
        self.__mats.append(Disciplina(cod, nome, ch, optativa))

    def getCargaHorarioTot(self):
        total = 0
        for each in self.__mats:
            if(each.getOp() == True):
                total += each.getCh()
        print('O total de horas do curso eh: {}'.format(total))

    def getCargaHorario(self):
        total = 0
        for each in self.__mats:
            total += each.getCh()
        return total


class Historico:
    def __init__(self, curso) -> None:
        self.__curso = curso

class Aluno:
    def __init__(self, matricula, nome , curso):
        self.__mat = matricula
        self.__nome = nome
        self.__curso = curso

        self.__hist = []
        self.__grade = ''

    def getGrade(self):
        return self.__grade

    def getName(self):
        return self.__nome

    def setGrade(self , nome):
        self.__grade =  nome

    def getMat(self):
        return self.__mat

    def addHistorico(self, cod, nome, ch, optativa):
        self.__hist.append(Disciplina(cod, nome, ch, optativa))

    def getHist(self):
        for each in self.__hist:
            print(each.getName() , each.getCh())
    
    def getCh(self):
        total = 0
        for each in self.__hist:
            if(each.getOp()):
                total += each.getCh()
        print('Carga horaria total obrigatoria realizada: {}'.format(total))


class Curso:
    def __init__(self, nome) -> None:
        self.__name = nome
        self.__grade = []

    def addDisc(self, cod, nome, ch, optativa):
        self.__grade.append(Disciplina(cod, nome, ch, optativa))

    def getName(self):
        return self.__name

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



class empDomestica(ABC):
    def __init__(self, nome, telefone):
        self.name = nome
        self.tele = telefone
        #Não tenho o costume de usar __ nas variaveis e escrevo em ingles o que funciona no trabalho das variaveis e em portugues no que o cliente enxerga
    
    def getName(self):
        return self.name
    
    def setName(self, nome):
        self.name = nome
    
    def getTele(self):
        return self.tele
    
    def setTele(self, tele):
        self.tele = tele
    #metodo abstrato
    @abstractmethod
    def getSalario(self):
        pass

class horista(empDomestica):
    def __init__(self, nome, telefone, horaTrabalhada , valorHora):
        super().__init__(nome, telefone)
        self.hourWork = horaTrabalhada
        self.hourPrice = valorHora
    
    #getters
    def getHoraTrabalhada(self):
        return self.hourWork

    def getPrecoHora(self):
        return self.hourPrice
    
    #setters
    def setHoraTrabalhada(self , horaTrabalhada):
        self.hourWork = horaTrabalhada

    def setPrecoHora(self, valorHora):
        self.hourPrice = valorHora
    
    #Julguei importante os getters e setters nesse caso, pois o usuário pode
    #querer alterar informações já cadastradas no sistema ao inves de criar 
    #outra variavel
    
    #polimorfismo
    def getSalario(self):
        return (self.hourPrice * self.hourWork)

class diarista(empDomestica):
    def __init__(self, nome, telefone, diasTrabalhados , valorDia):
        super().__init__(nome, telefone)
        self.dayWork = diasTrabalhados
        self.dayValue = valorDia
    
    #getters
    def getDiaTrabalhado(self):
        return self.dayWork

    def getValorDia(self):
        return self.dayValue
    
    #setters
    def setDiaTrabalhado(self , diasTrabalhados):
        self.dayWork = diasTrabalhados

    def setValorDia(self, valorDia):
        self.dayValue = valorDia
    
    #polimorfismo
    def getSalario(self):
        return (self.dayValue * self.dayWork)

class mensalista(empDomestica):
    def __init__(self, nome, telefone, salarioMes):
        super().__init__(nome, telefone)
        self.salario = salarioMes
    #polimorfismo
    def getSalario(self):
        return self.salario

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