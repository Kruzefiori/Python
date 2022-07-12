from lib2to3.pgen2.literals import simple_escapes
import tkinter as tk
from tkinter import messagebox
import os.path
import pickle
from tkinter import simpledialog
from xml.dom import NotFoundErr
class NoDisci(Exception):
    pass
class NotFound(Exception):
    pass
class Curso():
    def __init__(self, nome, anoGrade):
        self.nome = nome
        self.ano = anoGrade
        self.grade = []
    def getNome(self):
        return self.nome
    def getAnoGrade(self):
        return self.ano
    def getGrade(self):
        return self.grade
class LimiteInsereCurso(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('500x500')
        self.title("Curso")
        self.controle = controle
        self.frameNome = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameAno.pack()
        self.frameButton.pack()
        self.labelNome = tk.Label(self.frameNome, text='Curso: ')
        self.labelNome.pack(side='left')
        self.labelAno = tk.Label(self.frameAno, text='Grade: ')
        self.labelAno.pack(side='left')
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side='left')
        self.inputAno = tk.Entry(self.frameAno, width=15)
        self.inputAno.pack(side='left')
        self.btnSubmit = tk.Button(self.frameButton, text='Enter')
        self.btnSubmit.pack(side='left')
        self.btnSubmit.bind('<Button>', controle.enterHandler)
        self.btnClear = tk.Button(self.frameButton, text='Clear')
        self.btnClear.pack(side='left')
        self.btnClear.bind('<Button>', controle.clearHandler)    
        self.btnClose = tk.Button(self.frameButton, text='Close')
        self.btnClose.pack(side='left')
        self.btnClose.bind('<Button>', controle.closeHandler)
class ctrlCurso():
    def __init__(self, controlePrincipal):
        if not os.path.isfile('cursos.pickle'):
            self.listaCursos = []
        else:
            with open('cursos.pickle', 'rb') as f:
                self.listaCursos = pickle.load(f)      
        self.ctrlPrincipal = controlePrincipal        
    def salvaCursos(self):
        if len(self.listaCursos) != 0:
            with open('cursos.pickle', "wb") as f:
                pickle.dump(self.listaCursos, f)
    def getListaCursos(self):
        return self.listaCursos
    def getListaNomeCursos(self):
        listNome = []
        for each in self.listaCursos:
            listNome.append(each.getNome())
        return listNome
    def insereCurso(self):
        self.limiteInsCur = LimiteInsereCurso(self)
    def consultaCurso(self):
        cursoProc = simpledialog.askstring("Curso", "Informe o nome do curso: ")
        listaDisci = self.ctrlPrincipal.ctrlDisciplina.getListaDisci()
        try:
            for each in self.listaCursos:
                if cursoProc not in self.getListaNomeCursos():
                    raise NotFound
                else:
                    disciplinasDoCurso = []
                    for each in listaDisci:
                        if each.getCurso() == cursoProc:
                            disciplinasDoCurso.append(each)
                    info = ''
                    x = 1
                    for disci in disciplinasDoCurso:
                        info += 'Disciplina ' + str(x)  + '\nNome: ' + disci.getNome() + "\n" + "Código: " + disci.getCod() + "\n" + "Carga Horária: " + str(disci.getCarga()) + "\n" + '\n=====================\n' 
                        x += 1
                    if info == '':
                        raise NoDisci
                    messagebox.showinfo("Disciplinas", info)
        except NoDisci:
            messagebox.showerror("Vazio", "O curso ainda não possui disciplinas!")
        except NotFound:
            messagebox.showerror("Não encontrada", "O curso não existe!")
    def enterHandler(self, event):
        nome = self.limiteInsCur.inputNome.get()
        ano = self.limiteInsCur.inputAno.get()
        curso = Curso(nome, ano)
        self.listaCursos.append(curso)
        messagebox.showinfo("Concluído", "Curso inserido com sucesso!")
        self.clearHandler(event)
    def clearHandler(self, event):
        self.limiteInsCur.inputNome.delete(0, len(self.limiteInsCur.inputNome.get()))
        self.limiteInsCur.inputAno.delete(0, len(self.limiteInsCur.inputAno.get()))
    def closeHandler(self, event):
        self.limiteInsCur.destroy()        