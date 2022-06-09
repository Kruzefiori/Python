
class Motocicleta:
    
    # construtor
    def __init__(self, marca, cor, motorLigado):
        self.__marca = marca
        self.__cor = cor 
        self.__motorLigado = motorLigado

    # método de instância
    def ligaMotor(self):
        if self.__motorLigado == True:
            print('O motor já está ligado!')
        else:
            self.__motorLigado = True
            print('O motor acaba de ser ligado!')

    # método de instância
    def mostraAtributos(self):
        print('Esta motocicleta é uma {} {}'.format(self.__marca, self.__cor))
        if(self.__motorLigado):
            print('Seu motor está ligado')
        else:
            print('Seu motor está desligado')


if __name__ == "__main__":
    moto1 = Motocicleta('Honda', 'vermelha', False)
    moto1.mostraAtributos()
    print()
    moto1.ligaMotor()
    print()
    moto1.mostraAtributos()
    print()
    moto1.ligaMotor()