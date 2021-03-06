import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Produto():
    def __init__(self, cod=int, desc=str, valor=float):
        self.cod = cod
        self.desc = desc
        self.valor = valor
    
    def getCod(self):
        return self.cod
    
    def getDescr(self):
        return self.desc
    
    def getVal(self):
        return self.valor
    
class LimiteInsereProduto(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title('Produto')
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameDesc = tk.Frame(self)
        self.frameValor = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameValor.pack()
        self.frameDesc.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text='Codigo: ')
        self.labelCodigo.pack(side='left')
        self.labelDesc = tk.Label(self.frameDesc, text='Descrição: ')
        self.labelDesc.pack(side='left')
        self.labelValor = tk.Label(self.frameValor, text='Valor: ')
        self.labelValor.pack(side='left')

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputCodigo.pack(side='left')
        self.inputDesc = tk.Entry(self.frameDesc, width=25)
        self.inputDesc.pack(side='left')
        self.inputValor = tk.Entry(self.frameValor, width=20)
        self.inputValor.pack(side='left')

        self.btnCadastrar = tk.Button(self.frameButton, text='Cadastrar produto')
        self.btnCadastrar.pack(side='left')
        self.btnCadastrar.bind('<Button>', controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

class ControleProduto():
    def __init__(self):
        self.listaProd = []
                    
    def cadastraProd(self):
        self.limiteCad = LimiteInsereProduto(self)
        
    def getNomeProd(self):
        self.listaNomes = []
        for each in self.listaProd:
            self.listaNomes.append(each.getDescr())
        return self.listaNomes

    def getListaProd(self):
        return self.listaProd    
        
    def getCodigos(self):
        self.listaCodigos = []
        for each in self.listaProd:
            self.listaCodigos.append(each.getCod())
        return self.listaCodigos
    
    def consultaProd(self):
        produto = simpledialog.askstring('Código', 'Digite o código do produto: ')
        if produto not in self.getCodigos():
            messagebox.showinfo('Erro' , 'Produto não encontrado')
        else:
            for each in self.listaProd:
                    if each.getCod() == produto:
                        messagebox.showinfo(each.getDescr(), "Descrição: " + each.getDescr() + "\nCodigo: " + each.getCod() + "\nValor: R$" + each.getVal() + ",00")

    def enterHandler(self, event):
            cod = self.limiteCad.inputCodigo.get()
            desc = self.limiteCad.inputDesc.get()
            valor = self.limiteCad.inputValor.get()
            if cod == '' or desc == '' or valor == '':
                messagebox.showwarning("ERRO!", "Todos os campos devem ser preenchidos!")
            else:
                produto = Produto(cod, desc, valor)
                self.listaProd.append(produto)
                messagebox.showinfo("Sucesso!", "O produto foi cadastrado!")
                self.clearHandler(event)
            
    def clearHandler(self, event):
        self.limiteCad.inputCodigo.delete(0, len(self.limiteCad.inputCodigo.get()))
        self.limiteCad.inputDesc.delete(0, len(self.limiteCad.inputDesc.get()))
        self.limiteCad.inputValor.delete(0, len(self.limiteCad.inputValor.get()))

    def fechaHandler(self, event):
         self.limiteCad.destroy()
        