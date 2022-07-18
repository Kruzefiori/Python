import tkinter as tk
from tkinter import messagebox
import classe_padrão as classe #alterar para o arquivo da classe ou adicionar mais se tiver classes diferentes
""" import os.path
import pickle"""

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('500x550')
        self.menubar = tk.Menu(self.root)        
        self.MENU_NOME = tk.Menu(self.menubar)#TODO Cria a menu bar e coloca nela as opções
        #self.MENU_NOMEB = tk.Menu(self.menubar)#TODO
        #self.MENU_NOMEC= tk.Menu(self.menubar)#TODO   

        self.MENU_NOME.add_command(label="COMANDO",command=self.controle.FUNCAO)#TODO 
        #self.MENU_NOME.add_command(label="COMANDO",command=self.controle.FUNCAO)

        self.menubar.add_cascade(label="LABEL DENTRO DA CASCATA", \
                    menu=self.MENU_NOME)       

        """ self.sairMenu.add_command(label="Salva", 
                    command=self.controle.salvaDados)   #Exemplo de como é um sair
        self.menubar.add_cascade(label="Sair", 
                    menu=self.sairMenu) """

        self.root.config(menu=self.menubar) #configura o menu

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        """ self.ctrlEstudante = est.CtrlEstudante() #PEGA DA CLASSE E COLOCA AQUI O CONTROLADOR DELA
        self.ctrlDisciplina = disc.CtrlDisciplina()
        self.ctrlTurma = trm.CtrlTurma(self) """
        self.ctrlALGO = classe.ctrlALGO(self)
        self.limite = LimitePrincipal(self.root, self) #liga o limite principal

        self.root.title("P2")
        # Inicia o mainloop
        self.root.mainloop()
       
    def FUNCAO(self):#APERTAR O BOTÃO LEVA AQUI
        self.ctrlALGO.insereALGO()

    """ def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()     #EXEMPLO DE CÓDIGO PARA E COMO ADICIONAR,
                                                    #sempre pegar o controlador da classe e chamar ele aqui
    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

    def mostraTurmas(self):
        self.ctrlTurma.mostraTurmas() """

    def salvaDados(self):
        self.ctrlEstudante.salvaEstudantes()
        self.ctrlDisciplina.salvaDisciplinas()  #Se precisar de salvamento
        self.ctrlTurma.salvaTurmas()
        self.root.destroy()

if __name__ == '__main__':
    c = ControlePrincipal()