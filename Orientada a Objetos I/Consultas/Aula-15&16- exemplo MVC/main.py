import tkinter as tk
from tkinter import messagebox
import estudante as est
import disciplina as dis

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x200')
        self.menubar = tk.Menu(self.root)        
        self.estudanteMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.turmaMenu = tk.Menu(self.menubar)     

        self.estudanteMenu.add_command(label="Insere", \
                    command=self.controle.insereEstudantes)
        self.estudanteMenu.add_command(label="Mostra", \
                    command=self.controle.mostraEstudantes)
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        self.discipMenu.add_command(label="Insere",command=self.controle.insereDisciplinas)
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)
        self.discipMenu.add_command(label="Mostra", \
                    command=self.controle.mostraDisciplinas)

        self.turmaMenu.add_command(label="Insere")
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)        

        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEstudante = est.CtrlEstudante()
        self.ctrlDiscipi = dis.CtrlDisciplina()

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()
       
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDiscipi.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDiscipi.mostraDisciplinas()

if __name__ == '__main__':
    c = ControlePrincipal()