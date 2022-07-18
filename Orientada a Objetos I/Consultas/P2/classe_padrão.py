import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import simpledialog

#TALVEZ APAGAR
class NoDisci(Exception):
    pass
class NotFound(Exception): # Exemplos de exception
    pass 

class CLASSE_NOME():#TODO
    def __init__(self, A, B ):
        self.A = A
        self.B = B
        self.OBJETO = []

    #GETTERS APENAS AQUI DENTRO DA CLASSE 
    #GETTERS:

class limiteInsereALGO(tk.Toplevel):#MUDAR O ALGO
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("TITULO")#TODO
        self.controle = controle
        self.FRAMEA = tk.Frame(self)
        self.FRAMEB = tk.Frame(self)
        #self.FRAMEC = tk.Frame(self)...
        self.frameButton = tk.Frame(self)


        self.FRAMEA.pack()
        self.FRAMEB.pack()
        #self.FRAMEC.pack()...
        self.frameButton.pack()


        self.LABELA = tk.Label(self.FRAMEA, text='LABELA: ')#TODO
        self.LABELA.pack(side='left')
        self.LABELB = tk.Label(self.FRAMEB, text='LABELB: ')#TODO
        self.LABELB.pack(side='left')
        #self.LABELC = tk.Label(self.frameAno, text='LABELC: ')...
        #self.LABELC.pack(side='left')...


        self.INPUTA = tk.Entry(self.FRAMEA, width=20)#TODO
        self.INPUTA.pack(side='left')#TODO
        self.INPUTB = tk.Entry(self.FRAMEB, width=15)#TODO
        self.INPUTB.pack(side='left')#TODO
        #self.INPUTC = tk.Entry(self.frameAno, width=15)...
        #self.INPUTC.pack(side='left')...

        #BUTTONS AQUI COM TRES COMANDO PADROES JÁ PRONTOS
        self.btnSubmit = tk.Button(self.frameButton, text='Enter')#TODO
        self.btnSubmit.pack(side='left')#TODO
        self.btnSubmit.bind('<Button>', controle.enterHandler)#TODO

        self.btnClear = tk.Button(self.frameButton, text='Clear')
        self.btnClear.pack(side='left')
        self.btnClear.bind('<Button>', controle.clearHandler)   

        self.btnClose = tk.Button(self.frameButton, text='Close')
        self.btnClose.pack(side='left')
        self.btnClose.bind('<Button>', controle.closeHandler)


class ctrlALGO():
    def __init__(self, controlePrincipal):
        if not os.path.isfile('file.pickle'):#FILE DO PICKLE SE PRECISAR
            self.listaALGO = []
        else:
            with open('cursos.pickle', 'rb') as f:#TODO
                self.listaALGO = pickle.load(f)
        #SE NÃO PRECISAR DO PICKLE COMENTA DAQUI PRA CIMA E SO DEIXA A LINHA DEBAIXO      
        self.ctrlPrincipal = controlePrincipal   

    def salvaALGO(self):#TODO
        if len(self.listaALGO) != 0:
            with open('cursos.pickle', "wb") as f:
                pickle.dump(self.listaALGO, f)

    def getListaALGO(self):#TODO
        return self.listaALGO

    def getListaALGO(self):#TODO
        listACHADOS = []
        for each in self.listaALGO:
            listACHADOS.append(each)#.getA())
        return listACHADOS

    def insereALGO(self):#TODO
        self.limiteInsALGO = limiteInsereALGO(self)#TODO

    def consultaAlgo(self):#TODO
        algoProcurado = simpledialog.askstring("ALGO", "Informe o nome de ALGO: ")
        listaALGOS = self.ctrlPrincipal#.ctrlDisciplina.getListaDisci() EXEMPLO -> CONTROLE DE ALGO MAIS GET DE ALGO2
        try:
            for each in self.listaCursos:
                if algoProcurado not in self:#self com getter do que está procurando
                    raise NotFound
                else:
                    listaX = []
                    for each in listaALGOS:
                        if each.getCurso() == algoProcurado:
                            listaX.append(each) #ESSA PARTE DO MEIO É LÓGICA E VAI ALTERAR PARA CADA PROBLEMA
                    info = ''
                    x = 1
                    for disci in listaX:
                        info += 'Disciplina ' + str(x)  + '\nNome: ' + disci.getNome() + "\n" + "Código: " + disci.getCod() + "\n" + "Carga Horária: " + str(disci.getCarga()) + "\n" + '\n=====================\n' 
                        x += 1
                    if info == '':
                        raise NoDisci
                    messagebox.showinfo("Disciplinas", info)
                    #Há exemplos melhores em outros trabalhos, não recomendo tentar entender a lógica aqui
        except NoDisci:
            messagebox.showerror("EXCEPTION TESTE", "MENSAGEM DO EXCEPTION!")
        except NotFound:
            messagebox.showerror("EXCEPTION TESTE 2", "MENSAGEM DO EXCEPTION! 2")
    def enterHandler(self, event):
        A = self.limiteInsALGO.INPUTA.get() #mudar esses A e B e adicionar mais no mesmo padrão caso necessário
        B = self.limiteInsALGO.INPUTB.get()#TODO
        classe = CLASSE_NOME(A, B)#TODO
        self.listaALGO.append(classe)
        messagebox.showinfo("Concluído", "ALGO inserido com sucesso!")#TODO
        self.clearHandler(event)
    def clearHandler(self, event):#TODO
        self.limiteInsALGO.INPUTA.delete(0, len(self.limiteInsALGO.INPUTA.get()))#TODO
        self.limiteInsALGO.INPUTB.delete(0, len(self.limiteInsALGO.INPUTB.get()))#TODO
        #self.limiteInsALGO.INPUTC.delete(0, len(self.limiteInsALGO.INPUTC.get()))...
    def closeHandler(self, event):#TODO
        self.limiteInsALGO.destroy()  #TODO      