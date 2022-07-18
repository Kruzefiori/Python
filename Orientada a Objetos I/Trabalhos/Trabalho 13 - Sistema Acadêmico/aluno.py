from ast import While
import tkinter as tk
from tkinter import ACTIVE, messagebox, ttk, simpledialog
import os.path
import pickle
class NotExist(Exception):
    pass
class Aluno():
    def __init__(self, nome, nroMat):
        self.nome = nome
        self.numMat = nroMat
        self.historico = []
    def getNome(self):
        return self.nome
    def getNumMat(self):
        return self.numMat
    def getHistorico(self):
        return self.historico
class DisciCursada():
    def __init__(self, nome, ano, semestre, nota):
        self.nome = nome
        self.ano = ano
        self.semestre = semestre
        self.nota = nota
    def getNome(self):
        return self.nome
    def getAno(self):
        return self.ano
    def getSemestre(self):
        return self.semestre
    def getNota(self):
        return self.nota
class LimiteInsereAluno(tk.Toplevel):
        def __init__(self, controle): 
            tk.Toplevel.__init__(self)
            self.geometry('500x500')
            self.title('Aluno')
            self.controle = controle
            self.frameNome = tk.Frame(self)
            self.frameNro = tk.Frame(self)
            self.frameButton = tk.Frame(self)
            self.frameNome.pack()
            self.frameNro.pack()
            self.frameButton.pack()
            self.labelNome = tk.Label(self.frameNome, text="Nome: ")
            self.labelNro = tk.Label(self.frameNro, text='Número: ')
            self.labelNome.pack(side='left')         
            self.labelNro.pack(side='left')        
            self.inputNome = tk.Entry(self.frameNome, width=20)
            self.inputNro = tk.Entry(self.frameNro, width=15)
            self.inputNome.pack(side='left')
            self.inputNro.pack(side='left')
            self.btnEnter = tk.Button(self.frameButton, text='Enter')
            self.btnEnter.pack(side='left')
            self.btnEnter.bind("<Button>", controle.enterHandler)
            self.btnClear = tk.Button(self.frameButton, text='Clear')
            self.btnClear.pack(side='left')
            self.btnClear.bind('<Button>', controle.clearHandler)
            self.btnClose = tk.Button(self.frameButton, text='Close')
            self.btnClose.pack(side='left')
            self.btnClose.bind('<Button>', controle.closeHandlerIns)
class LimiteAddDisci(tk.Toplevel):
    def __init__(self, controle, listaDisci):
        tk.Toplevel.__init__(self)
        self.geometry('500x250')
        self.title('Disciplina Cursada')
        self.controle = controle
        self.frameListaDisci = tk.Frame(self)
        self.frameNota = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameSemestre = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameListaDisci.pack()
        self.frameNota.pack()
        self.frameButton.pack()
        self.labelLista = tk.Label(self.frameListaDisci, text='Lista de Disciplinas')
        self.labelLista.pack(side='left')
        self.labelNota = tk.Label(self.frameNota, text="Nota: ")
        self.labelNota.pack(side='left')
        self.labelAno = tk.Label(self.frameAno, text='Ano: ')
        self.labelAno.pack(side='left')
        self.labelSemestre = tk.Label(self.frameSemestre, text='Semestre: ')
        self.labelSemestre.pack(side='left')
        self.inputLista = ttk.Combobox(self.frameListaDisci, width=30)
        self.inputLista.set('Escolha uma disciplina')
        self.inputLista.pack(side='left')
        self.inputLista['values'] = listaDisci
        self.inputNota = tk.Entry(self.frameNota, width=20)
        self.inputNota.pack(side='left')
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side='left')
        self.inputSemestre = tk.Entry(self.frameSemestre, width=20)
        self.inputSemestre.pack(side='left')
        self.btnSubmit = tk.Button(self.frameButton, text='Enter')
        self.btnSubmit.pack(side='left')
        self.btnSubmit.bind('<Button>', controle.insereHandler)
        self.btnClear = tk.Button(self.frameButton, text='Clear')
        self.btnClear.pack(side='left')
        self.btnClear.bind('<Button>', controle.clearHandler)
        self.btnClose = tk.Button(self.frameButton, text='Close')
        self.btnClose.pack(side='left')
        self.btnClose.bind('<Button>', controle.closeHandlerDisc)
class CtrlAluno():
    def __init__(self, controlePrincipal):
        if not os.path.isfile('aluno.pickle'):
            self.listaAlunos = []
        else:
            with open('aluno.pickle', "rb") as f:
                self.listaAlunos = pickle.load(f)               
        self.ctrlPrincipal = controlePrincipal
    def salvaAlunos(self):
        if len(self.listaAlunos) != 0:
            with open("aluno.pickle", "wb") as f:
                pickle.dump(self.listaAlunos, f)
    def getAluno(self, numMat):
        procurado = None
        for aluno in self.listaAlunos:
            if aluno.getNumMat() == numMat:
                procurado = aluno
        return procurado
    def getListaMat(self, listaAluno):
        listaMat = []
        for each in listaAluno:
            listaMat.append(each.getNumMat())
        return listaMat
    def getListaAlunos(self):
        return self.listaAlunos
    def insereAluno(self):
        self.limiteIns = LimiteInsereAluno(self)
    def insereDisciAluno(self):
        listaDisci = []
        listaDisci = self.ctrlPrincipal.ctrlDisciplina.getListaNomeDisci()
        self.limInsDis = LimiteAddDisci(self, listaDisci)
    def consultaAluno(self):
        ask = True
        while ask == True:
            numMat = simpledialog.askstring("Número", "Informe a matrícula do aluno: ")
            try:
                pontAluno = self.getAluno(numMat)
                if pontAluno == None:
                    raise NotExist
                else:
                    info = ""
                    cargaTot = 0
                    historico = pontAluno.getHistorico() 
                    for disci in historico:
                        for disciplina in self.ctrlPrincipal.ctrlDisciplina.getListaDisci():
                            infoDisci = ""
                            if disci.getNome() == disciplina.getNome():
                                cod = disciplina.getCod()
                                carga = disciplina.getCarga()
                                nota = disci.getNota()
                                infoDisci += '\n' + "Disciplina: " + disci.getNome() + "\n" + "Código: " + cod + "\n" + "Nota: " + nota + "\n-----------------------------"
                            info += infoDisci
                        cargaTot += int(carga)
                    return messagebox.showinfo('Info', 'Histórico: ' + str(info))
            except NotExist:
                messagebox.showerror("Não encontrado", " A matrícula não pertence a nenhum aluno!")
                ask = messagebox.askyesno('Continuar?', "Deseja tentar novamente?")
    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        numMat = self.limiteIns.inputNro.get()
        aluno = Aluno(nome, numMat)
        self.listaAlunos.append(aluno)
        messagebox.showinfo("OK", "Aluno incluido!")
        self.clearHandler(event)
    def insereHandler(self, event):
        numAluno = simpledialog.askstring("Aluno", "Digite a matrícula do aluno: ")
        try:
            aluno = self.getAluno(numAluno)
            if aluno == None:
                raise NotExist
            nome = self.limInsDis.inputLista.get()
            ano = self.limInsDis.inputAno.get()
            semestre = self.limInsDis.inputSemestre.get()
            nota = self.limInsDis.inputNota.get()
            disci = DisciCursada(nome, ano, semestre, nota)
            aluno.getHistorico().append(disci)
            messagebox.showinfo("OK", "Disciplina adicionada ao histórico de " + aluno.getNome())
        except NotExist:
            messagebox.showerror("Não encontrado", " A matrícula não pertence a nenhum aluno!")
    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))    
    def clearHandlerDisc(self, event):
        self.limInsDis.inputLista.set('Escolha uma disciplina')
        self.limInsDis.inputAno.delete(0, len(self.limInsDis.inputAno.get()))
        self.limInsDis.inputSemestre.delete(0, len(self.limInsDis.inputSemestre.get()))
        self.limInsDis.inputNota.delete(0, len(self.limInsDis.inputNota.get()))        
    def closeHandlerIns(self, event):
        self.limiteIns.destroy()  
    def closeHandlerDisc(self, event):
        self.limInsDis.destroy()