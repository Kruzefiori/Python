lista = ['a', 0, 2]

for elemento in lista:
    try:
        print("O elemento é ", elemento)
        r = 1/int(elemento)
        break
    except Exception as e:
        print("Oops!", e.__class__, "ocorreu")
        print("Próxima entrada")
        print()
print("O número recíproco de", elemento , "é", r)