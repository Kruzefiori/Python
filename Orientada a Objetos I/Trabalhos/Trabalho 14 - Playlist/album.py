import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os.path
import pickle

class Musica:
    def __init__(self, nome, nroFaixa, artista):
        self.__nome = nome
        self.__nroFaixa = nroFaixa
        self.__artista = artista

    def getNome(self):
        return self.__nome

    def getNroFaixa(self):
        return self.__nroFaixa
    
    def getArtista(self):
        return self.__artista

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano
        self.__listaMusicas = []

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista
    
    def getAno(self):
        return self.__ano

    def getMusicas(self):
        return self.__listaMusicas
    
    def getNroFaixa(self):
        return len(self.__listaMusicas) + 1

    def insereMusica(self, faixas):
        return self.__listaMusicas.append(faixas)
    

class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x100')
        self.title("Cadastra álbum")
        self.controle = controle

        self.frameArtista = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameButton.pack()
        
        self.labelArtista = tk.Label(self.frameArtista, text="Artista: ")
        self.labelTitulo = tk.Label(self.frameTitulo, text="Título: ")
        self.labelAno = tk.Label(self.frameAno, text="Ano:")
        self.labelArtista.pack(side="left")  
        self.labelTitulo.pack(side="left")
        self.labelAno.pack(side="left")
        
        self.inputArtista = tk.Entry(self.frameArtista, width=20)
        self.inputArtista.pack(side="left")             
        self.inputTitulo = tk.Entry(self.frameTitulo, width=20)
        self.inputTitulo.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left") 
        
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerCad)
      
        self.buttonClear = tk.Button(self.frameButton, text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerCad)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x75')
        self.title("Consulta Álbum")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Título do Álbum: ")
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

class LimiteInsereFaixa(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x75')
        self.title("Insere Faixa")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome do música: ")
        self.labelNome.pack(side="left")  

        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandlerInsert)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandlerInsert)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.closeHandlerInsert)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlAlbum():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        
        if not os.path.isfile("album.pickle"):
            self.listaAlbuns = []
            self.listaMscs = []
        else:
            with open("album.pickle", "rb") as f:
                self.listaAlbuns = pickle.load(f)
                self.listaMscs = pickle.load(f)
    
    def salvaAlbuns(self):
        if len(self.listaAlbuns) != 0:
            with open("album.pickle","wb") as f:
                pickle.dump(self.listaAlbuns, f)
                pickle.dump(self.listaMscs, f)

    def getAlbuns(self):
        return self.listaAlbuns
    
    def getMscs(self):
        return self.listaMscs
    
    def getFaixa(self, nome):
        for msc in self.listaMscs:
            if msc.getNome() == nome:
                return msc
        return None
    
    def cadastraAlbum(self):
        self.limiteCad = LimiteCadastraAlbum(self)

    def enterHandlerCad(self, event):
        ano = self.limiteCad.inputAno.get()
        titulo = self.limiteCad.inputTitulo.get()
        artista = self.limiteCad.inputArtista.get()
        if len(ano) != 0 and len(titulo) != 0 and len(artista) != 0: 
            artistaSel = self.ctrlPrincipal.ctrlArtista.getArtista(artista)
            if artistaSel != None:
                album = Album(titulo, artistaSel, ano)
                self.listaAlbuns.append(album)
                artistaSel.insereAlbum(album)
                self.limiteCad.mostraJanela("Sucesso","Álbum criado com sucesso! Insira as faixas!")
                self.closeHandlerCad(event)
                self.limiteInsert = LimiteInsereFaixa(self)
            else:
                self.limiteCad.mostraJanela("Falha", "Artista inválid!o")
                self.clearHandlerCad(event)
        else:
            self.limiteCad.mostraJanela("Falha", "Dados inválidos!")
            self.clearHandlerCad(event)

    def clearHandlerCad(self, event):
        self.limiteCad.inputAno.delete(0, len(self.limiteCad.inputAno.get()))
        self.limiteCad.inputTitulo.delete(0, len(self.limiteCad.inputTitulo.get()))
        self.limiteCad.inputArtista.delete(0, len(self.limiteCad.inputArtista.get()))

    def closeHandlerCad(self, event):
        self.limiteCad.destroy()
    
    def enterHandlerInsert(self, event):
        nome = self.limiteInsert.inputNome.get()
        nroFaixa = self.listaAlbuns[-1].getNroFaixa()
        artista = self.listaAlbuns[-1].getArtista()
        musica = Musica(nome, nroFaixa, artista)
        self.listaAlbuns[-1].insereMusica(musica)
        self.listaMscs.append(musica)
        self.limiteInsert.mostraJanela("Sucesso", "Faixa inserida no Álbum")
        self.clearHandlerInsert(event)

    def clearHandlerInsert(self, event):
        self.limiteInsert.inputNome.delete(0, len(self.limiteInsert.inputNome.get()))

    def closeHandlerInsert(self, event):
        self.limiteInsert.destroy()

    def consultaAlbum(self):
        self.limiteCon = LimiteConsultaAlbum(self)

    def enterHandlerCon(self, event):
        titulo = self.limiteCon.inputNome.get()
        if len(titulo) != 0:
            for album in self.listaAlbuns:
                if album.getTitulo() == titulo:
                    str1 = "Álbum " + album.getTitulo()
                    str2 = "Ano:" + album.getAno() + "\nFaixas:\n"
                    listaFaixas = album.getMusicas()
                    for msc in listaFaixas:
                        str2 += str(msc.getNroFaixa()) + " - " +  msc.getNome() + "\n"
                    self.limiteCon.mostraJanela(str1, str2)
                    self.clearHandlerCon(event)
                    return
            self.limiteCon.mostraJanela("Falha", "Álbum não encontrado!")
            self.clearHandlerCon(event)
        else:
            self.limiteCon.mostraJanela("Falha", "Título inválido!")
            self.clearHandlerCon(event)

    def clearHandlerCon(self, event):
        self.limiteCon.inputNome.delete(0, len(self.limiteCon.inputNome.get()))

    def closeHandlerCon(self, event):
        self.limiteCon.destroy()
