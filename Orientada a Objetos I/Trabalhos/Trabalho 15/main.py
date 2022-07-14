from cProfile import label
import tkinter as tk
import produto as produto

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x500')
        self.menubar = tk.Menu(self.root)
        self.produtoMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        self.produtoMenu.add_command(label='Insere', command=self.controle.insereproduto)
        self.produtoMenu.add_command(label='Consultar', command=self.controle.consultaproduto)
        self.menubar.add_cascade(label='produto', menu=self.produtoMenu)
        self.sairMenu.add_command(label='Salvar', command=self.controle.salvaDados)
        self.menubar.add_cascade(label='Sair', menu=self.sairMenu)
        self.root.config(menu=self.menubar)

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlproduto = produto.CtrlProd(self)
        self.limiteIns = LimitePrincipal(self.root, self)
        self.root.title('Trabalho 15 - produtos e notas fiscais')
        self.root.mainloop()

    def insereproduto(self):
        self.ctrlproduto.insereproduto()
    
    def consultaproduto(self):
        self.ctrlproduto.consultaproduto()
    
    def salvaDados(self):
        self.ctrlproduto.salvaprodutos()
        self.root.destroy()
if __name__ == '__main__':
    c = ControlePrincipal()