import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Produto:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self.desc = descricao
        self.val = valor

        self.ṕrods = []
        
    def getCodigo(self):
        return self.codigo

    def getDesc(self):
        return self.desc

    def getValor(self):
        return self.val

    def getProd(self):
        return "Desc: " + str(self.getDesc())\
        + "\nCodigo: " + str(self.getCodigo())\
        + "\Valor: " + str(self.getValor())\


class LimiteInsereproduto(tk.Toplevel):
        def __init__(self, controle): 
            tk.Toplevel.__init__(self)
            self.geometry('500x500')
            self.title('produto')
            self.controle = controle
            self.frameDesc = tk.Frame(self)
            self.frameVal = tk.Frame(self)
            self.frameCod = tk.Frame(self)
            self.frameButton = tk.Frame(self)

            self.frameDesc.pack()
            self.frameVal.pack()
            self.frameCod.pack()
            self.frameButton.pack()

            self.labelDesc = tk.Label(self.frameDesc, text="Desc: ")
            self.labelVal = tk.Label(self.frameVal, text='Valor: ')
            self.labelCod = tk.Label(self.frameCod, text='Codigo: ')       
            self.labelDesc.pack(side='left')
            self.labelVal.pack(side='left')
            self.labelCod.pack(side='left')

            self.inputDesc = tk.Entry(self.frameDesc, width=20)
            self.inputVal = tk.Entry(self.frameVal, width=15)
            self.inputCod = tk.Entry(self.frameCod, width=15)

            self.inputDesc.pack(side='left')
            self.inputVal.pack(side='left')
            self.inputCod.pack(side='left')
            
            self.btnEnter = tk.Button(self.frameButton, text='Enter')
            self.btnEnter.pack(side='left')
            self.btnEnter.bind("<Button>", controle.enterHandler)
            self.btnClear = tk.Button(self.frameButton, text='Clear')
            self.btnClear.pack(side='left')
            self.btnClear.bind('<Button>', controle.clearHandler)
            self.btnClose = tk.Button(self.frameButton, text='Close')
            self.btnClose.pack(side='left')
            self.btnClose.bind('<Button>', controle.closeHandlerIns)

class CtrlProd():
    def __init__(self, controlador):
        self.controlador = controlador

        self.prods =  []
    
    def insereproduto(self):
        self.limiteIns = LimiteInsereproduto(self)

    def enterHandler(self, event):
        codigo = self.limiteIns.inputCod.get()
        valor = self.limiteIns.inputVal.get()
        desc = self.limiteIns.inputDesc.get()
        self.prods.append(Produto(codigo , desc , valor))
            
    def clearHandler(self, event):
        self.limiteIns.inputCod.delete(0, len(self.limiteIns.inputCod.get()))
        self.limiteIns.inputVal.delete(0, len(self.limiteIns.inputVal.get()))
        self.limiteIns.inputDesc.delete(0, len(self.limiteIns.inputDesc.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeTipo(self,event):
        print(self.limiteCons.inputTipo.get())
            

    #def exibeVariedade(self, event):