
def mdc(m, n):
    while m%n != 0:
        oldm = m
        oldn = n
        m = oldn
        n = oldm%oldn
    return n

def mesmaFracao(f1, f2):
    return (f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())


class Fracao():
    
    def __init__(self , num , den  , inteiro = None ):
        self.__num = num        
        self.__den = den
        self.__int = inteiro    

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den  

    def getInt(self):
        return self.__int 

    def __str__(self):
        if self.__int != None : 
            return str (self.__int) + ' ' + str(self.__num) + "/" + str(self.__den)
        else:
            return str(self.__num) + "/" + str(self.__den)    

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        if self.__int != None or outraFrac.__int != None:
            if self.__int != None: 
                inteiro = self.__int
            else:
                inteiro = 0
            if outraFrac.__int != None:
                inteiro2 = self.__int
            else:
                inteiro2 = 0
            novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum() + outraFrac.getNum() + self.__num + inteiro * outraFrac.getDen() + inteiro2 * self.__num
            novoDen = novoDen = self.__den * outraFrac.getDen()
            divComum = mdc(novoNum, novoDen)
            x=0
            varNum = novoNum
            varDen = novoDen
            while varNum > varDen:
                varNum -= novoDen
                x += 1
            return Fracao(novoNum//divComum, novoDen//divComum , x-1 )
        else:
            novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
            novoDen = self.__den * outraFrac.getDen()
            divComum = mdc(novoNum, novoDen)
            x=0
            varNum = novoNum
            varDen = novoDen
            while varNum > varDen:
                varNum -= novoDen
                x += 1
            return Fracao(novoNum//divComum, novoDen//divComum , x-1 )       

if __name__ == "__main__":
    frac1 = Fracao (1, 4) 
    frac2 = Fracao(1, 6)
    frac3 = frac1 + frac2
    #print(frac3)
    #print()
    frac1 = Fracao (3, 4)
    frac2 = Fracao(5, 6)
    frac3 = frac1 + frac2
    #print(frac3)
    #print()
    fracmista = Fracao( 2 , 3 , 4)
    #print(fracmista)
    #print(fracmista + frac1)
    fracA = Fracao (1 , 2)
    fracB = Fracao(3 , 4)
    print((fracA + fracB))
    
    