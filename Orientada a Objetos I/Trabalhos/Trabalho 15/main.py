import tkinter as tk
import produto as prod
import cupom as cupom

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)
        self.menuProduto = tk.Menu(self.menubar)
        self.menuCupom = tk.Menu(self.menubar)

        self.menuProduto.add_command(label='Cadastrar', command= self.controle.cadastraProd)
        self.menuProduto.add_command(label='Consultar', command= self.controle.consultaProd)
        self.menubar.add_cascade(label='Produtos', menu=self.menuProduto)
        
        self.menuCupom.add_command(label='Criar', command= self.controle.iniciaCupom)
        self.menuCupom.add_command(label='Consultar', command= self.controle.consultaCupom)
        self.menubar.add_cascade(label='Cupom Fiscal', menu=self.menuCupom)
        
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlProduto = prod.ControleProduto()
        self.ctrlCupom = cupom.ControleCupom(self)
        self.limitePrincipal = LimitePrincipal(self.root, self)
        self.root.title('Trabalho 15 - Cupom Fiscal')
        self.root.mainloop()
    
    def cadastraProd(self):
        self.ctrlProduto.cadastraProd()
    def consultaProd(self):
        self.ctrlProduto.consultaProd()
    def iniciaCupom(self):
        self.ctrlCupom.iniciaCupom()
    def consultaCupom(self):
        self.ctrlCupom.consultaCupom()

if __name__ == '__main__':
    c = ControlePrincipal()
        
