from abc import ABC, abstractmethod
from tokenize import Number

class Professor(ABC):
    def __init__(self, nome, matricula, cargaHoraria):
        self.__nome = nome
        self.__matricula = matricula
        self.__cargaHoraria = cargaHoraria

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula

    def getCargaHoraria(self):
        return self.__cargaHoraria

    @abstractmethod
    def getSalario(self):
        pass

class ProfDE(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioBruto):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioBruto

    def setSalario(self, salario):
        self.__salarioBruto = salario

    def getSalario(self):
        if self.__salarioBruto < 1903.98:
            imposto = 0
        elif self.__salarioBruto < 2826.65:
            imposto = ((self.__salarioBruto/100)* 7.5)
        elif self.__salarioBruto < 3751.05:
             imposto = ((self.__salarioBruto/100)* 15)
        elif self.__salarioBruto < 4664.68:
            imposto = ((self.__salarioBruto/100)* 22.5)
        elif self.__salarioBruto > 4664.68:
            imposto = ((self.__salarioBruto/100)* 27.5)
        return (self.__salarioBruto - ((self.__salarioBruto/100)*11)) - imposto

class ProfHorista(Professor):
    def __init__(self, nome, matricula, cargaHoraria, salarioHora):
        super().__init__(nome, matricula, cargaHoraria)
        self.__salarioBruto = salarioHora

    def setSalarioHora(self, salarioHora):
        self.__salarioBruto = salarioHora 

    def getSalarioHora(self):
        return self.__salarioBruto

    def getSalario(self):
        imposto = Number
        if self.__salarioBruto * self.getCargaHoraria() < 1903.98:
            imposto = 0
        elif self.__salarioBruto * self.getCargaHoraria() < 2826.65:
            imposto = ((self.__salarioBruto * self.getCargaHoraria()/100)* 7.5)
        elif self.__salarioBruto * self.getCargaHoraria() < 3751.05:
             imposto = ((self.__salarioBruto * self.getCargaHoraria()/100)* 15)
        elif self.__salarioBruto * self.getCargaHoraria() < 4664.68:
            imposto = ((self.__salarioBruto * self.getCargaHoraria()/100)* 22.5)
        elif self.__salarioBruto * self.getCargaHoraria() > 4664.68:
            imposto = ((self.__salarioBruto * self.getCargaHoraria()/100)* 27.5)
        return ((self.__salarioBruto * self.getCargaHoraria()) - imposto)

if __name__ == "__main__":
    prof1 = ProfDE('Joao', 12345, 40, 5000)
    prof2 = ProfHorista('Paulo', 54321, 30, 75)
    prof3 = ProfHorista('Ana', 56789, 38, 95)
    profs = [prof1 ,prof2, prof3]
    for prof in profs:
        print ('Nome: {} - Salário: {}'.format(prof.getNome(), prof.getSalario()))

