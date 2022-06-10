class Animal:

    #construtor
    def __init__(self,nome):
        self.__nome = nome

    #getter
    def getNome(self):
        return self.__nome

    #metodo
    def fazerCarinho(self):
        print("{} está recebendo carinho".format(self.__nome))

class Gato(Animal):

    #construtor
    def __init__(self, nome):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)

    #método
    def miar(self):
        print("Meow Meow")

class Cao(Animal):

    #construtor
    def __init__(self, nome):
        #super é usado para permitir acessar métodos 
        #e propriedades da superclasse
        super().__init__(nome)

    #método
    def latir(self):
        print("Au Au")     

if __name__ == "__main__":
    gato = Gato("Perola")
    print(gato.getNome())
    gato.miar()
    gato.fazerCarinho()
    cao = Cao("Cleitin")
    print(cao.getNome())    
    cao.latir()    
    cao.fazerCarinho()