# tk02.py
# Usando classes para criar interfaces
import tkinter as tk

class GUI:
   def __init__(self):
      # Cria a janela
      self.janela = tk.Tk()
      
      # Note que a janela é passada como argumento na 
      # criação do widget
      self.label = tk.Label(self.janela, text="Hello world", font=("Arial Bold", 50))
      
      # Chama o método pack()
      self.label.pack()
      
      # Entra no mainloop, o que faz com que 
      # a janela seja renderizada na tela
      self.janela.mainloop()

def main():
   GUI()

main()