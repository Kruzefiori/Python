import tkinter as tk
from tkinter import messagebox
import os.path
import pickle


class Artista:
    def __init__(self, nome):
        self.__nome = nome 
        self.__albuns = []
    
    def getNome(self):
        return self.__nome

    def getAlbuns(self):
        return self.__albuns
    
    def insereAlbum(self, album):
        self.__albuns.append(album)

class LimiteCadastraArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x75')
        self.title("Cadastrar Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerCad)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerCad)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.closeHandlerCad)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x75')
        self.title("Consulta Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerCon)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerCon)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.closeHandlerCon)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista():
    def __init__(self):
        if not os.path.isfile("artista.pickle"):
            self.listaArtistas = []
        else:
            with open("artista.pickle", "rb") as f:
                self.listaArtistas = pickle.load(f)
    
    def salvaArtistas(self):
        if len(self.listaArtistas) != 0:
            with open("artista.pickle","wb") as f:
                pickle.dump(self.listaArtistas, f)

    #Getters Úteis
    def getArtistas(self):
        return self.listaArtistas
    
    def getArtista(self, nome):
        for artista in self.listaArtistas:
            if artista.getNome() == nome:
                return artista
        return None
    
    def getNomesArtistas(self):
        if len(self.listaArtistas) != 0:
            nomesArtistas = []
            for artista in self.listaArtistas:
                nomesArtistas.append(artista.getNome())
            return nomesArtistas
        else: return None

    def cadastraArtista(self):
        self.limiteCad = LimiteCadastraArtista(self)

    def enterHandlerCad(self, event):
        nome = self.limiteCad.inputNome.get()
        artista = Artista(nome)
        if len(nome) != 0:
            for artista in self.listaArtistas:
                if artista.getNome() == nome:
                    self.limiteCad.mostraJanela("ERRO", "Artista já cadastrado!")
                    self.clearHandlerCad(event)
                    return
            artista = Artista(nome)
            self.listaArtistas.append(artista)
            self.limiteCad.mostraJanela("Sucesso", "Artista cadastrado!")
            self.clearHandlerCad(event)
        else:
            self.limiteCad.mostraJanela("ERRO", "Digite algum nome!")
            self.clearHandlerCad(event)  


    def clearHandlerCad(self, event):
        self.limiteCad.inputNome.delete(0, len(self.limiteCad.inputNome.get()))

    def closeHandlerCad(self, event):
        self.limiteCad.destroy()

    def consultaArtista(self):
        self.limiteCon = LimiteConsultaArtista(self)

    def enterHandlerCon(self, event):
        Nome = self.limiteCon.inputNome.get()
        if len(Nome) != 0:
            for artista in self.listaArtistas:
                if artista.getNome() == Nome:
                    str1 = "Albuns do artista:" + artista.getNome()
                    str2 = "Artista: " + artista.getNome()
                    if len(artista.getAlbuns()) != 0:
                        for album in artista.getAlbuns():
                            str2 += "\nÁlbum: " + album.getTitulo() + " --- " + album.getAno() + "\n"
                            str2 += "Faixas: \n"
                            for faixas in album.getMusicas():
                                str2 += "|" + str(faixas.getNroFaixa()) + " - " + faixas.getNome() + "|\n"
                        self.limiteCon.mostraJanela(str1, str2)
                        self.clearHandlerCon(event)
                        return
                    else:
                        self.limiteCon.mostraJanela("Falha", "Artista não possui albuns!")
                        self.clearHandlerCon(event)
                        return
            self.limiteCon.mostraJanela("Falha", "Nome inválido!")
            self.clearHandlerCon(event)
        else:
            self.limiteCon.mostraJanela("Falha", "Dado inválido!")
            self.clearHandlerCon(event)

    def clearHandlerCon(self, event):
        self.limiteCon.inputNome.delete(0, len(self.limiteCon.inputNome.get()))

    def closeHandlerCon(self, event):
        self.limiteCon.destroy()
