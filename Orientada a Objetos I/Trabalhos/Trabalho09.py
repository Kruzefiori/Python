from abc import ABC, abstractclassmethod

class titulo_nao_doutor(Exception):
    pass

class idade_inferior(Exception):
    pass

class curso_nao_aceito(Exception):
    pass

class cpf_duplicado(Exception):
    pass

class Pessoa(ABC):

    def __init__(self , name, adr , age , cpf) -> None:
        self.__name = name 
        self.__adr = adr
        self.__age = age 
        self.__cpf = cpf
    
    def getName(self):
        return self.__name

    def getAdr(self):
        return self.__adr
    
    def getAge(self):
        return self.__age

    def getCpf(self):
        return self.__cpf

    @abstractclassmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):
    def __init__(self, name, adr, age, cpf , tit) -> None:
        super().__init__(name, adr, age, cpf)
        self.__tit = tit

    def getTit(self):
        return self.__tit

    def printDescricao(self):
        print('Nome: {} \nEndereço: {}\nidade: {}\nCpf: {}\nTitulo: {}\n'.format(self.getName(), self.getAdr() ,self.getAge(),
         self.getCpf(), self.getTit()))

class Aluno(Pessoa):
    def __init__(self, name, adr, age, cpf , curso) -> None:
        super().__init__(name, adr, age, cpf)
        self.__cur = curso

    def getCurso(self):
        return self.__cur

    def printDescricao(self):
        print('Nome: {} \nEndereço: {}\nidade: {}\nCpf: {}\nCurso: {}\n'.format(self.getName(), self.getAdr() ,self.getAge(),
         self.getCpf(), self.getCurso()))

if __name__ == '__main__':
    cadastrados = []
    ListaExemplo = [
        ('Victor' , 'Rua Jose' , 22 , 74185296398 , 'SIN'),#Sucesso
        ('Marcos' , 'Rua Joao' , 21 , 74185296398 , 'SIN'),#Erro mesmo cpf
        ('Josias' , 'Rua Maria' , 22 , 25698743562 , 'ENG'),#Erro de curso diferente
        ('Leopoldo' , 'Rua Joana' , 24 , 15963248746 , 'CCO'),#Sucesso
        ('Mathias' , 'Rua Gabriela' , 28 , 74184226398 , 'SIN'),#Sucesso
        ('Geraldo' , 'Rua Majela' , 17 , 77185296398 , 'SIN'),#Erro idade inferior
    ]

    ListaExemploDois = [
        ('Kruze' , 'Rua Tobias' , 45 , 14632587412 , 'Doutorado'), #Sucesso
        ('Matheus' , 'Rua Marcelo' , 63 , 74185296398 , 'Doutorado'),#erro de cpf duplicado
        ('Josias' , 'Rua Elizabeth' , 40 , 15632456321 , 'Mestrado'),#erro de titulo invalido
        ('Leonidas' , 'Rua Fiona' , 24 , 95636248502 , 'Doutorado'),#Erro de idade inferior
        ('Matusalem' , 'Rua Pereira' , 30 , 158746875621 , 'Doutorado'),#Sucesso
        ('Roberto' , 'Rua Magda' , 55 , 20123695874 , 'Doutorado'),#Sucesso
    ]

    for name, end , age , cpf , curso in ListaExemplo:
        try:
            if cpf in cadastrados:
                raise cpf_duplicado()
            if age < 18:
                raise idade_inferior()
            if curso != ('SIN' or 'CCO'):
                raise curso_nao_aceito()
        except idade_inferior:
            print('Idade inferior a 18 anos! {} do usuario:{}\n'.format(age , name))
        except cpf_duplicado:
            print('Cpf já cadastrado no sistema {} do usuario:{}\n'.format(cpf, name))
        except curso_nao_aceito:
            print('Curso não aceito no cadastro {} do usuario:{}\n'.format(curso, name))
        else:
            newAluno = Aluno(name, end, age, cpf, curso)
            cadastrados.append(newAluno)
            print('Usuário %s cadastrado com sucesso\n' %name)

    for name, end , age , cpf , titulo in ListaExemploDois:
        try:
            if cpf in cadastrados:
                raise cpf_duplicado()
            if age < 30:
                raise idade_inferior()
            if titulo != 'Doutorado':
                raise titulo_nao_doutor()
        except idade_inferior:
            print('Idade inferior a 30 anos! {} do usuario:{}\n'.format(age , name))
        except cpf_duplicado:
            print('Cpf já cadastrado no sistema {} do usuario:{}\n'.format(cpf, name))
        except titulo_nao_doutor:
            print('Titulo não aceito no cadastro {} do usuario: {}\n'.format(titulo , name))
        else:
            newprof = Professor(name, end, age, cpf, titulo)
            cadastrados.append(newprof)
            print('Usuário %s cadastrado com sucesso\n' %name)

    for each in cadastrados:
        each.printDescricao()