# importar module sys para pegar o tipo da exception
import sys

lista = ['a', 0, 2]

for elemento in lista:
    try:
        print("O elemento é ", elemento)
        r = 1/int(elemento)
        break
    except:
        print("Oops!", sys.exc_info()[0], "ocorreu")
        print("Próxima entrada")
        print()
print("O número recíproco de", elemento , "é", r)