from cProfile import label
import tkinter as tk
import aluno as aluno
import curso as curso
import disciplina as dis
class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x500')
        self.menubar = tk.Menu(self.root)
        self.alunoMenu = tk.Menu(self.menubar)
        self.cursoMenu = tk.Menu(self.menubar)
        self.disciplinaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)
        self.alunoMenu.add_command(label='Insere', command=self.controle.insereAluno)
        self.alunoMenu.add_command(label='Add disciplina', command=self.controle.insereDisciAluno)
        self.alunoMenu.add_command(label='Consultar', command=self.controle.consultaAluno)
        self.menubar.add_cascade(label='Aluno', menu=self.alunoMenu)
        self.cursoMenu.add_command(label='Insere', command=self.controle.insereCurso)
        self.cursoMenu.add_command(label='Consulta', command=self.controle.consultaCurso)
        self.menubar.add_cascade(label='Curso', menu=self.cursoMenu)
        self.disciplinaMenu.add_command(label='Insere', command=self.controle.insereDisciplina)
        self.menubar.add_cascade(label='Disciplina', menu=self.disciplinaMenu)
        self.sairMenu.add_command(label='Salvar', command=self.controle.salvaDados)
        self.menubar.add_cascade(label='Sair', menu=self.sairMenu)
        self.root.config(menu=self.menubar)
class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()
        self.ctrlAluno = aluno.CtrlAluno(self)
        self.ctrlDisciplina = dis.ctrlDisciplina(self)
        self.ctrlCurso = curso.ctrlCurso(self)
        self.limite = LimitePrincipal(self.root, self)
        self.root.title('Trabalho Sistema Acadêmico')
        self.root.mainloop()
    def insereAluno(self):
        self.ctrlAluno.insereAluno()
    def insereDisciAluno(self):
        self.ctrlAluno.insereDisciAluno()
    def consultaAluno(self):
        self.ctrlAluno.consultaAluno()
    def insereDisciplina(self):
        self.ctrlDisciplina.insereDisciplina()
    def insereCurso(self):
        self.ctrlCurso.insereCurso()
    def consultaCurso(self):
        self.ctrlCurso.consultaCurso()
    def salvaDados(self):
        self.ctrlAluno.salvaAlunos()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlCurso.salvaCursos()
        self.root.destroy()
if __name__ == '__main__':
    c = ControlePrincipal()
        

