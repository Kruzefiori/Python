import tkinter as tk
from tkinter import messagebox , simpledialog

class ModelCliente():
    def __init__(self, nome, email , cod):
        self.__nome = nome
        self.__email = email
        self.__cod = cod

    def getNome(self):
        return self.__nome

    def getEmail(self):
        return self.__email

    def getCod(self):
        return self.__cod

    def getInfo(self):
        return f'Cliente: ' + self.getNome() + '\nEmail: ' + self.getEmail() + '\nCódigo: '+ self.getCod()

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame4 = tk.Frame(self.janela)
        self.frame5 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Código: ")
        self.labelInfo4 = tk.Label(self.frame4,text="---------------------------")
        self.labelInfo5 = tk.Label(self.frame5,text="Buscar Cliente por código:")
        
        self.labelInfo1.pack(side="left")
        self.labelInfo2.pack(side="left")  
        self.labelInfo3.pack(side="left")
        self.labelInfo4.pack(side="left")
        self.labelInfo5.pack(side="left")

        self.inputText1 = tk.Entry(self.frame1, width=20)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=20)
        self.inputText2.pack(side="left") 
        self.inputText3 = tk.Entry(self.frame3, width=20)
        self.inputText3.pack(side="left")  
        self.inputText4 = tk.Entry(self.frame5, width=20)
        self.inputText4.pack(side="left")  
           
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  

        self.buttonList = tk.Button(self.janela,text="Mostrar Clientes")      
        self.buttonList.pack(side="left")
        self.buttonList.bind("<Button>", controller.clientesHandler) 

        self.buttonCli = tk.Button(self.janela,text="Consultar Cliente por código")      
        self.buttonCli.pack(side="left")
        self.buttonCli.bind("<Button>", controller.consultaCliente) 

        # Ex2: Acrescentar o botão para listar os clientes cadastrados           

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)

      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x200')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC - Trabalho 10 - Victor Kruze Fiori")
        # Inicia o mainloop
        self.root.mainloop()

    def consultaCliente(self , event): 
        cod = self.view.inputText4.get()
        cont = 0
        for each in self.listaClientes:
            if each.getCod() == cod:
                nome = each.getNome()
                messagebox.showinfo('Cliente: ', each.getInfo())
                cont+= 1
        if cont == 0:
           messagebox.showerror('erro', 'Codigo nao Cadastrado')
    

    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get()
        emailCli = self.view.inputText2.get()
        cod = self.view.inputText3.get()
        cliente = ModelCliente(nomeCli, emailCli, cod)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))
    
    # Ex2: implementar função para listar os clientes cadastrados
    def clientesHandler(self, event):
        lista = ''
        for each in self.listaClientes:
            lista += 'Nome:'+ each.getNome() + '\nEmail: ' + each.getEmail() +'\nCódigo: ' + each.getCod() + '\n-------------------'
        self.view.mostraJanela('Lista de cadastrados:',lista)
    
if __name__ == '__main__':
    c = Controller()