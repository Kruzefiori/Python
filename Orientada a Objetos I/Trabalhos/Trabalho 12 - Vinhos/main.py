import tkinter as tk
import vinho as vin

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.vinhoMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        self.vinhoMenu.add_command(label="Cadastrar", command=self.controle.cadastraVinho)
        self.vinhoMenu.add_command(label="Consultar", command=self.controle.consultaVinho)
        self.menubar.add_cascade(label="Vinho", menu=self.vinhoMenu)
        
        self.root.config(menu=self.menubar)
      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlVinho = vin.CtrlVinho(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Prova 2")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraVinho(self):
        self.ctrlVinho.cadastraVinho()
    
    def consultaVinho(self):
        self.ctrlVinho.consultaVinho()


if __name__ == '__main__':
    c = ControlePrincipal()