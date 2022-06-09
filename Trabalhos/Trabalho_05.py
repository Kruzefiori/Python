from abc import ABC, abstractmethod


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

if __name__ == "__main__":
    #cadastro de empregados
    empHorista = horista('Margaret Thatcher' , '35 70707070' , 160 , 10)
    empDiariata = diarista('Leonardo da Vinci' , '35 71717171' , 20 , 55)
    empMensalista = mensalista('Amelia Earhart' , '35 72727272' , 1000)
    listaSal = []
    #lista com todos
    listaEmp = [empHorista , empDiariata , empMensalista]
    print('opcoes:')
    for each in listaEmp:
        print ('Nome: {} - Salario: {}'.format(each.getName(), each.getSalario()))
        listaSal.append(each.getSalario())
    
    listaSal.sort() #Coloca a lista de salario de forma ordenada
    for each in listaEmp:#for que acha de quem é o melhor salário
        if each.getSalario() == listaSal[0]:
            choose = each
            break
            
    print('A melhor opcao eh: \n Nome: {} \n Telefone: {} \n Com o salario de: {}'.format(choose.getName() , choose.getTele() , choose.getSalario()));
