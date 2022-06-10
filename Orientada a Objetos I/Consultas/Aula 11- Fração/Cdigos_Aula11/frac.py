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
    def __init__(self, num, den):

        self.__num = num        
        self.__den = den     

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def getNum(self):
        return self.__num

    def getDen(self):
        return self.__den

    def simplifica(self):
        divComum = mdc(self.__num, self.__den)
        self.__num = self.__num // divComum
        self.__den = self.__den // divComum   

    def __add__(self,outraFrac):
        novoNum = self.__num * outraFrac.getDen() + self.__den * outraFrac.getNum()
        novoDen = self.__den * outraFrac.getDen()
        divComum = mdc(novoNum, novoDen)
        return Fracao(novoNum//divComum, novoDen//divComum)          

if __name__ == "__main__":
    frac1 = Fracao(3,4)
    frac2 = Fracao(3,4)
    print(mesmaFracao(frac1, frac1))
    print(frac1 is frac2)
    frac1 = frac2
    print(frac1 is frac2)