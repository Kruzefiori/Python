import tkinter as tk
from tkinter import messagebox
import estudante as est
import disciplina as disc
import turma as trm

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.estudanteMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.turmaMenu = tk.Menu(self.menubar)
        self.consultaMenu = tk.Menu(self.menubar)   

        self.estudanteMenu.add_command(label="Insere", \
                    command=self.controle.insereEstudantes)
        self.estudanteMenu.add_command(label="Mostra", \
                    command=self.controle.mostraEstudantes)
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        self.discipMenu.add_command(label="Insere", \
                    command=self.controle.insereDisciplinas)
        self.discipMenu.add_command(label="Mostra", \
                    command=self.controle.mostraDisciplinas)        
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        self.turmaMenu.add_command(label="Insere", \
                    command=self.controle.insereTurmas)
        self.turmaMenu.add_command(label="Mostra", \
                    command=self.controle.mostraTurmas)                     
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)        

        self.consultaMenu.add_command(label="Busca Aluno", \
                    command=self.controle.buscaAluno)
        self.consultaMenu.add_command(label="Busca Disciplina", \
                    command=self.controle.buscaDisciplina)                
        self.consultaMenu.add_command(label="Busca Turma", \
                    command=self.controle.buscaTurma)                          
        self.menubar.add_cascade(label="Buscar", \
                    menu=self.consultaMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEstudante = est.CtrlEstudante()
        self.ctrlDisciplina = disc.CtrlDisciplina()
        self.ctrlTurma = trm.CtrlTurma(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def buscaAluno(self):
        self.ctrlEstudante.buscaAluno()

    def buscaDisciplina(self):
        self.ctrlDisciplina.buscaDisciplina()

    def buscaTurma(self):
        self.ctrlTurma.buscaTurma()
    
       
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

    def mostraTurmas(self):
        self.ctrlTurma.mostraTurmas()

if __name__ == '__main__':
    c = ControlePrincipal()