# tk07.py
import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.janela = tk.Tk()

        # Cria dois frames, um para os checkbuttons
        # e outro para o botão
        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)
        
        # Cria 3 objetos IntVar para usar com os checkbuttons    
        self.cbVar1 = tk.IntVar()
        self.cbVar2 = tk.IntVar()
        self.cbVar3 = tk.IntVar()
        
        # Ajusta os IntVar objetos para 0
        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)
        
        # Cria os Checkbuttons no frameTopo
        self.cb1 = tk.Checkbutton(self.frameTopo, \
                    text='Opção 1', variable=self.cbVar1)
        self.cb2 = tk.Checkbutton(self.frameTopo, \
                    text='Opção 2', variable=self.cbVar2)
        self.cb3 = tk.Checkbutton(self.frameTopo, \
                    text='Opção 3', variable=self.cbVar3)

        # Empacota os Checkbuttons
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # Cria botões Ok e Finaliza
        self.okButton = tk.Button(self.frameBase, \
                      text='OK', command=self.mostraEscolha)
        self.finalizaButton = tk.Button(self.frameBase, \
                      text='Finaliza', command=self.janela.destroy)

        # Empacota os botões
        self.okButton.pack(side='left')
        self.finalizaButton.pack(side='left')

        # Empacota os frames
        self.frameTopo.pack()
        self.frameBase.pack()
        
        # Inicia o mainloop
        tk.mainloop()

    # Função de callback para o okButton    
    def mostraEscolha(self):
        # cria uma mensagem
        self.message = 'Você selecionou:\n'
        # Verifica quais CheckButtons foram selecionados
        # e monta a mensagem 
        if self.cbVar1.get() == 1:
            self.message = self.message + '1\n'
        if self.cbVar2.get() == 1:
            self.message = self.message + '2\n'
        if self.cbVar3.get() == 1:
            self.message = self.message + '3\n'
        # Mostra a mensagem no messagebox
        messagebox.showinfo('Seleção', self.message)

def main():
   MyGUI()

main()