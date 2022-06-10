# imprime o número recíproco apenas de números pares

try:
    num = int(input("Digite um número: "))
    assert num % 2 == 0
except:
    print("Não é um número par!")
else:
    reciproco = 1/num
    print(reciproco)