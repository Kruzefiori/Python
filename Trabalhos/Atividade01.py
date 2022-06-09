from sys import exit
    
def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:
        aux = array[j]
        array[j] = array[j+1]
        array[j+1] = aux    

valor = input('Digite um valor qualquer:\nDigito 0 encerra o programa')# primeira leitura do valor
valor = int(valor)
if valor == 0:
    print('Nenhum valor para ser ordenado, programa finalizado!')
    exit()
respostas = []
respostas.append(valor)
while valor != 0:
    leitura = input('Digite um valor qualquer:')
    valor = int(leitura)
    if valor != 0:
        respostas.append(valor)
    
print('array não ordenado:')
print(respostas) #printa o array de valores lidos na ordem que foram lidos

bubbleSort(respostas)

print('array ordenado através do Bubble Sort:')
print(respostas)
