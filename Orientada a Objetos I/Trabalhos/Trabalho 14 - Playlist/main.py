import tkinter as tk
from tkinter import messagebox
import album as alb
import playlist as play
import artista as art

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x500')
        self.menubar = tk.Menu(self.root)        
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)     

        self.artistaMenu.add_command(label="Cadastrar Artista", \
                    command=self.controle.cadastraArtistas)
        self.artistaMenu.add_command(label="Consultar Artista", \
                    command=self.controle.consultaArtista)
        self.menubar.add_cascade(label="Artista", \
                    menu=self.artistaMenu)

        self.albumMenu.add_command(label="Cadastrar Album", \
                    command=self.controle.cadastraAlbums)  
        self.albumMenu.add_command(label="Consultar Album", \
                    command=self.controle.consultaAlbum)    
        self.menubar.add_cascade(label="Album", \
                    menu=self.albumMenu)

        self.playlistMenu.add_command(label="Cadastrar Playlist", \
                    command=self.controle.cadastraPlaylists) 
        self.playlistMenu.add_command(label="Consultar Playlist",\
                    command=self.controle.consultaPlaylist)                   
        self.menubar.add_cascade(label="Playlist", \
                    menu=self.playlistMenu)

        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu) 
        self.sairMenu.add_command(label="Salvar", \
                    command=self.controle.salvaDados)
          

        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlArtista = art.CtrlArtista()
        self.ctrlAlbum = alb.CtrlAlbum(self)
        self.ctrlPlaylist = play.CtrlPlaylist(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Trabalho 14 - Playlist")
        # Starta o mainloop
        self.root.mainloop()
       
    def cadastraArtistas(self):
        self.ctrlArtista.cadastraArtista()

    def consultaArtista(self):
        self.ctrlArtista.consultaArtista()

    def cadastraAlbums(self):
        self.ctrlAlbum.cadastraAlbum()

    def consultaAlbum(self):
        self.ctrlAlbum.consultaAlbum()

    def cadastraPlaylists(self):
        self.ctrlPlaylist.cadastraPlaylist()

    def consultaPlaylist(self):
        self.ctrlPlaylist.consultaPlaylist()

    def salvaDados(self):
        self.ctrlPlaylist.salvaPlaylists()
        self.ctrlAlbum.salvaAlbuns()
        self.ctrlArtista.salvaArtistas()
        self.root.destroy()

if __name__ == "__main__":
    c = ControlePrincipal()