class ValorMenor(Exception):
    #Gerada quando o valor é menor
    pass

class ValorMaior(Exception):
    #Gerada quando o valor é maior
    pass

# número a ser descoberto
nro = 10

# usuário tenta adivinhar o número
while True:
    try:
        i_num = int(input("Digite um número: "))
        if i_num < nro:
            raise ValorMenor
        elif i_num > nro:
            raise ValorMaior
        break
    except ValorMenor:
        print("Valor menor, tente novamente!")
        print()
    except ValorMaior:
        print("Valor maior, tente novamente!")
        print()

print("Parabéns! Você descobriu o número.")