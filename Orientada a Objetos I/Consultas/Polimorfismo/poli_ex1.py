from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome        
    
    @abstractmethod
    def visualizar(self):
        pass
    
class Pdf(Documento):
    def visualizar(self):
        return 'Mostra no Adobe Acrobat'

class Word(Documento):
    def visualizar(self):
        return 'Mostra no Word'

if __name__ == "__main__":
    documentos = [Pdf('PDF1'), Word('DOC1'), Pdf('PDF2')]
    for documento in documentos:
        print('{}: {}'.format(documento.getNome(), documento.visualizar()))