import tkinter as tk
from tkinter import messagebox, ttk
import os.path
import pickle
class Disciplina():
    def __init__(self, cod, nome, carga, curso):
        self.cod = cod
        self.nome = nome
        self.carga = carga
        self.curso = curso
    def getCod(self):
        return self.cod
    def getNome(self):
        return self.nome
    def getCarga(self):
        return self.carga
    def getCurso(self):
        return self.curso
class LimiteInsereDisci(tk.Toplevel):
    def __init__(self, controle, listaCursos):
        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title('Disciplina')
        self.controle = controle
        self.frameCod = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameCarga = tk.Frame(self)
        self.frameCurso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCod.pack()
        self.frameNome.pack()
        self.frameCarga.pack()
        self.frameCurso.pack()
        self.frameButton.pack()
        self.labelCod = tk.Label(self.frameCod, text='Código: ')
        self.labelCod.pack(side='left')
        self.labelNome = tk.Label(self.frameNome, text='Nome: ')
        self.labelNome.pack(side='left')
        self.labelCarga = tk.Label(self.frameCarga, text='Carga Horaria: ')
        self.labelCarga.pack(side='left')
        self.labelCurso = tk.Label(self.frameCurso, text='Curso: ')
        self.labelCurso.pack(side='left')
        self.inputCod = tk.Entry(self.frameCod, width=20)
        self.inputCod.pack(side='right')
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='right')
        self.inputCarga = tk.Entry(self.frameCarga, width=20)
        self.inputCarga.pack(side='right')
        self.inputCurso = ttk.Combobox(self.frameCurso, width=20)
        self.inputCurso.pack(side='right')
        self.inputCurso['values'] = listaCursos
        self.btnSubmit = tk.Button(self.frameButton, text='Enter')
        self.btnSubmit.pack(side='left')
        self.btnSubmit.bind('<Button>', controle.enterHandler)
        self.btnClear = tk.Button(self.frameButton, text='Clear')
        self.btnClear.pack(side='left')
        self.btnClear.bind('<Button>', controle.clearHandler)
        self.btnClose = tk.Button(self.frameButton, text='Close')
        self.btnClose.pack(side='left')
        self.btnClose.bind('<Button>', controle.closeHandler)
class ctrlDisciplina():
    def __init__(self, controlePrincipal):
        if not os.path.isfile('disciplinas.pickle'):
            self.listaDisci = []
        else:
            with open("disciplinas.pickle", "rb") as file:
                self.listaDisci = pickle.load(file)
        self.ctrlPrincipal = controlePrincipal
    def salvaDisciplinas(self):
        if len(self.listaDisci) != 0:
            with open('disciplinas.pickle', 'wb') as file:
                pickle.dump(self.listaDisci, file)
    def insereDisciplina(self):
        listaCursos = self.ctrlPrincipal.ctrlCurso.getListaNomeCursos()
        self.limiteInsDis = LimiteInsereDisci(self, self.listaDisci)
    def getListaDisci(self):
        return self.listaDisci
    def getListaNomeDisci(self):
        listname = []
        for each in self.listaDisci:
            listname.append(each.getNome())
        return listname
    def enterHandler(self, event):
        cod = self.limiteInsDis.inputCod.get()
        nome = self.limiteInsDis.inputNome.get()
        carga = self.limiteInsDis.inputCarga.get()
        curso = self.limiteInsDis.inputCurso.get()
        disci = Disciplina(cod, nome, carga, curso)
        self.listaDisci.append(disci)
        messagebox.showinfo("Concluído", "A disciplina foi cadastrada")
        self.clearHandler(event)
    def clearHandler(self, event):
        self.limiteInsDis.inputCod.delete(
            0, len(self.limiteInsDis.inputCod.get()))
        self.limiteInsDis.inputNome.delete(
            0, len(self.limiteInsDis.inputNome.get()))
        self.limiteInsDis.inputCarga.delete(
            0, len(self.limiteInsDis.inputCarga.get()))
        self.limiteInsDis.inputCurso.delete(
            0, len(self.limiteInsDis.inputCurso.get()))
    def closeHandler(self, event):
        self.limiteInsDis.destroy()