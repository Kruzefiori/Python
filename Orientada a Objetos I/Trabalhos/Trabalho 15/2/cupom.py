import tkinter as tk
from produto import EmptyField
from tkinter import END, messagebox, simpledialog, ttk
import os.path
import pickle


class Cupom():
    def __init__(self, num, listaProd):
        self.nro = num
        self.listaProd = listaProd
        
    def getNro(self):
        return self.nro
    
    def getListaProd(self):
        return self.listaProd

class LimiteCriaCupom(tk.Toplevel):
    def __init__(self, controle, listaprod, listaProdCup):
        
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title('Produto')
        self.controle = controle
        self.listaProd = listaprod #lista de produtos pré-definida
        
        #frame
        self.frameNum = tk.Frame(self)
        self.frameListaProd = tk.Frame(self)
        self.frameListaCupom = tk.Frame(self)  #lista de produtos adicionada no cupom
        self.frameButton = tk.Frame(self)
        
        #pack
        self.frameNum.pack()
        self.frameListaProd.pack()
        self.frameListaCupom.pack()
        self.frameButton.pack()
        
        #label
        self.labelNum = tk.Label(self.frameNum, text='Número do cupom: ')
        self.labelNum.pack(side='left')
        self.labelListaProd = tk.Label(self.frameListaProd, text='Adicionar: ')
        self.labelListaProd.pack(side='left')
        self.labelListaProdCup = tk.Label(self.frameListaCupom, text='Produtos:')
        self.labelListaProdCup.pack(side='left')
        
        self.inputNum = tk.Entry(self.frameNum, width=20)
        self.inputNum.pack(side='left')
        self.inputListaProd = ttk.Combobox(self.frameListaProd, width=20)
        self.inputListaProd.pack(side='left')
        self.inputListaProd['values'] = self.listaProd
        self.inputListaProd.set('Escolha um produto')
        self.outputListaProdCup = tk.Listbox(self.frameListaCupom)
        self.outputListaProdCup.pack(side='left')
        for each in listaProdCup:
            self.outputListaProdCup.insert(tk.END, each)
        
        self.btnAdicionar = tk.Button(self.frameButton, text='Adicionar')
        self.btnAdicionar.pack(side='left')
        self.btnAdicionar.bind('<Button>', controle.adicionaProd)
        
        self.btnLimpar = tk.Button(self.frameButton, text='Limpar')
        self.btnLimpar.pack(side='left')
        self.btnLimpar.bind('<Button>', controle.limparCupom)
        
        self.btnSair = tk.Button(self.frameButton, text='Finalizar Cupom')
        self.btnSair.pack(side='left')
        self.btnSair.bind('<Button>', controle.fechaCupom)
        

class CtrlCupom():
    
    def __init__(self, controlePrincipal):
        if not os.path.isfile('cupom.pickle'):
            self.listaCupons = []
        else:
            with open('cupom.pickle', "rb") as f:
                self.listaCupons = pickle.load(f)
        
        self.controlePrincipal = controlePrincipal
    
    def salvaCupons(self):
        if len(self.listaCupons) != 0:
            with open("cupom.pickle", "wb") as f:
                pickle.dump(self.listaCupons, f)
    
    def getListaProdCup(self):
        lista = self.listaProdCup
        return lista
                
    def iniciaCupom(self):
        self.listaProdCup = []
        self.criaCup = LimiteCriaCupom(self, self.controlePrincipal.ctrlProduto.getNomeProd(), self.getListaProdCup())
    
    def adicionaProd(self, event):
        produto = self.criaCup.inputListaProd.get()
        self.listaProdCup.append(produto)  
        self.criaCup.outputListaProdCup.insert(END, produto)
        messagebox.showinfo("Concluido", "Produto adicionado!")
        
    def fechaCupom(self, event):
        
        try:
            num = self.criaCup.inputNum.get()
            listaProd = self.criaCup.inputListaProd.get()
            
            if num == None or listaProd == '':
                raise EmptyField
            else:
                cupom = Cupom(num, listaProd)
                self.listaCupons.append(cupom)
                messagebox.showinfo('Feito!', "Cupom criado com sucesso!")
                self.limparCupom(event)
                
        except EmptyField:
            messagebox.showwarning("Vazio!", "Todos os campos devem ser preenchidos!")
            
    def limparCupom(self, event):
            self.criaCup.inputListaProd.set('---')
            self.criaCup.inputNum.delete(0, len(self.criaCup.inputNum.get()))
            self.criaCup.outputListaProdCup.delete(0, END)
            
    def consultaCupom(self):
        numero = simpledialog.askstring("Número", "Digite o número do cupom fiscal: ")
        
        for each in self.listaCupons:
            #Se o numero for igual
            if each.getNro() == numero:
                info = ''
                listaProdUnit = []
                valorTot = 0
                self.listaProdutosTotais = self.controlePrincipal.ctrlProduto.getListaProd()
                
                        
                #Coloca em uma lista os produtos sem repetição
                for produtoFinal in self.listaProdCup:
                    for produtoTotal in self.listaProdutosTotais:
                        if produtoFinal == produtoTotal.getDescr():
                            if produtoTotal not in listaProdUnit:
                                listaProdUnit.append(produtoTotal)
                
                #Para cada produto sem repetição
                for produtoUnico in listaProdUnit:
                    quantidade = self.listaProdCup.count(produtoUnico.getDescr()) #Conta as ocorrências do produto na lista completa
                    info += "Produto: " + produtoUnico.getDescr() + "\nCodigo: " + str(produtoUnico.getCod()) + "\nValor: R$" + str(produtoUnico.getVal()) + ",00\n" + "Quantidade: " + str(quantidade) + "\n----------------------\n"
                    valorTot += int(produtoUnico.getVal()) * int(quantidade)
                messagebox.showinfo("Produtos", info + "\n Valor total: " + str(valorTot))
                        
                

        
