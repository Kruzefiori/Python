import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicasPlay = []

    def getNome(self):
        return self.__nome
    
    def getMusicasPlay(self):
        return self.__musicasPlay
    
    def insereFaixas(self, faixas):
        for msc in faixas:
            self.__musicasPlay.append(msc)
        
class LimiteCadastraPlaylist(tk.Toplevel):
    def __init__(self, controle, listaNomesArtistas, listaFaixas):
        self.listaFaixas = listaFaixas

        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Playlist")
        self.controle = controle
        self.frameNome = tk.Frame(self)
        self.frameArtistas = tk.Frame(self)
        self.frameMusicas = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameArtistas.pack()
        self.frameMusicas.pack()
        self.frameButton.pack()        

        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        self.labelArtistas = tk.Label(self.frameArtistas,text="Artistas: ")
        self.labelArtistas.pack(side="left")
        self.escolhaCombo = tk.StringVar()
        self.combobox = ttk.Combobox(self.frameArtistas, width = 15 ,\
                                     textvariable = self.escolhaCombo)
        self.combobox.pack(side="left")
        self.combobox['values'] = listaNomesArtistas
        self.combobox.bind("<<ComboboxSelected>>", self.updateListBox)
          
        self.labelEst = tk.Label(self.frameMusicas,text="Musicas: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameMusicas)
        self.listbox.pack(side="left")

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereMusica)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaPlaylist)    
    
    def updateListBox(self, event):
        self.listbox.delete(0, tk.END)
        artistaSel = self.escolhaCombo.get()
        for faixas in self.listaFaixas:
            if faixas.getArtista().getNome() == artistaSel:
                self.listbox.insert(tk.END, faixas.getNome())

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)     

class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x75')
        self.title("Consulta Playlist")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNome = tk.Label(self.frameNome,text="Nome da playlist: ")
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

class CtrlPlaylist():
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        if not os.path.isfile("playlist.pickle"):
            self.listaPlay = []
        else:
            with open("playlist.pickle", "rb") as f:
                self.listaPlay = pickle.load(f)
    
    def salvaPlaylists(self):
        if len(self.listaPlay) != 0:
            with open("playlist.pickle","wb") as f:
                pickle.dump(self.listaPlay, f)
    
    def cadastraPlaylist(self):
        self.listaMusicasPlaylist = []
        listaNomesArtistas = self.ctrlPrincipal.ctrlArtista.getNomesArtistas()
        listaFaixas = self.ctrlPrincipal.ctrlAlbum.getMscs()
        self.limiteCad = LimiteCadastraPlaylist(self, listaNomesArtistas, listaFaixas)

    def insereMusica(self, event):
        faixaSel = self.limiteCad.listbox.get(tk.ACTIVE)
        faixa = self.ctrlPrincipal.ctrlAlbum.getFaixa(faixaSel)
        if faixa in self.listaMusicasPlaylist:
            self.limiteCad.mostraJanela('Alerta', 'Música já foi inserida!')
            self.limiteCad.listbox.delete(tk.ACTIVE)
        else:
            self.listaMusicasPlaylist.append(faixa)
            self.limiteCad.mostraJanela('Sucesso', 'Música inserida')
            self.limiteCad.listbox.delete(tk.ACTIVE)

    def criaPlaylist(self, event):
        nome = self.limiteCad.inputNome.get()
        playlist = Playlist(nome)
        playlist.insereFaixas(self.listaMusicasPlaylist)
        self.listaPlay.append(playlist)
        self.limiteCad.mostraJanela('Sucesso', 'Playlist criada com sucesso')
        self.limiteCad.destroy()

    def consultaPlaylist(self):
        self.limiteCon = LimiteConsultaPlaylist(self)

    def enterHandlerCon(self, event):
        nome = self.limiteCon.inputNome.get()
        if len(self.listaPlay) != 0:
            for playlist in self.listaPlay:
                if playlist.getNome() == nome:
                    str1 = "Playlist " + playlist.getNome()
                    str2 = "\nFaixas: \n"
                    nroFaixa = 1
                    for faixa in playlist.getMusicasPlay():
                        str2 += str(nroFaixa) + " --- " + faixa.getNome() + "\n"
                        nroFaixa += 1
                    self.limiteCon.mostraJanela(str1, str2)
                    self.clearHandlerCon(event)
                    return
            self.limiteCon.mostraJanela("Falha", "Playlist não encontrada!")
            self.clearHandlerCon(event)
        else:
            self.limiteCon.mostraJanela("Falha", "Não há playlists criadas!")
            self.clearHandlerCon(event)

    def clearHandlerCon(self, event):
        self.limiteCon.inputNome.delete(0, len(self.limiteCon.inputNome.get()))

    def closeHandlerCon(self, event):
        self.limiteCon.destroy()