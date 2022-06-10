from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, endereco, idade, listaDisc):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade    
        self.listaDisc = listaDisc    

    def getNome(self):
        return self.__nome

    def getEndereco(self):
        return self.__endereco

    def getIdade(self):
        return self.__idade

    def getLista(self):
        return self.listaDisc

    def insereDisc(self, disc):
        self.listaDisc.append(disc)

    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, titulacao , listaDisc):
        super().__init__(nome, endereco, idade , listaDisc)
        self.__titulacao = titulacao

    def getTitulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Titulação: {}'.format(self.getTitulacao()))
        print('Disciplinas ministradas:')
        listaDisc = self.getLista()
        for disc in listaDisc:
            print('Nome: {} - carga horária: {}'.format(disc.getNome(), disc.getCarga()))        

class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, curso, listaDisc):
        super().__init__(nome, endereco, idade, listaDisc)
        self.__curso = curso

    def getCurso(self):
        return self.__curso

    def printDescricao(self):
        print('Nome: {}'.format(self.getNome()))
        print('Endereço: {}'.format(self.getEndereco()))
        print('Idade: {}'.format(self.getIdade()))
        print('Curso: {}'.format(self.getCurso())) 
        print('Disciplinas cursadas:')
        listaDisc = self.getLista()
        for disc in listaDisc:
            print('Nome: {} - carga horária: {}'.format(disc.getNome(), disc.getCarga()))


class Disciplina():
    def __init__(self, nome, cargaHoraria):
        self.nome = nome
        self.cargaHoraria = cargaHoraria
    def getNome(self):
        return self.nome
    def getCarga(self):
        return self.cargaHoraria
    






if __name__ == "__main__":
    disc1 = Disciplina('Programação OO I' , 64)
    disc2 = Disciplina('Estrutura de dados' , 64)
    disc3 = Disciplina('Engenharia de software' , 48)
    prof = Professor('Andrey' , 'Av, BPS 1303' , 40 , 'Mestrado' , [])
    aluno = Aluno('Victor' , 'R José Verano Da Silva 266' , 22 , 'SIN' , [])
    prof.insereDisc(disc1)
    prof.insereDisc(disc3)
    aluno.insereDisc(disc1)
    aluno.insereDisc(disc2)
    prof.printDescricao()
    print()
    aluno.printDescricao()
    print()
