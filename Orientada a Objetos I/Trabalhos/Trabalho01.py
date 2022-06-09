class Veiculo:

    #construtor
    def __init__(self, marca, cor, motorLigado):

        self.__marca = marca
        self.__cor = cor 
        self.__motorLigado = motorLigado
    
    def getligaMotor(self):
        return self.__motorLigado

    def ligaMotor(self):
        if(self.__motorLigado):
            ask = print("Motor já ligado, deseja desligar?")
            if (ask == "S"):
                self.__motorLigado = False
            else:
                print("Mantemos o motor ligado")
        else:
            self.__motorLigado = True
    

class Carro(Veiculo):
    
    def __init__(self, marca, cor, motorLigado, portaMalasCheio, mostraAtributos):
        self.portaMalasCheio = portaMalasCheio
        super().__init__(marca, cor, motorLigado)

    def isPortaMalasCheio(self):
        return self.__portaMalasCheio

    def enchePortaMalas(self):
        if(self.__portaMalasCheio):
            print("Porta malas já está cheio ")
        else:
            self.portaMalasCheio = True
            print(" O porta malas acaba de ser preenchido")

    def getMarca(self):
        return self.__marca
    
    def getCor(self):
        return self.__cor
    
    def mostraAtributos(self):

        print("Este carro é um {} {}" .format(self.getMarca, self.getCor))

        print(Carro.getligaMotor)
        print(Carro.enchePortaMalas)

class Moto(Veiculo):

    def __init__(self, estilo, mostraAtributos):
        self.estilo = estilo

    def getEstilo(self):
        return self.estilo
    
    def mostraAtributos(self):
        print(Moto.getligaMotor)
        print(Moto.getEstilo)
            

    
