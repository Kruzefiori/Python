#Author: Victor Kruze Fiori - Mat = 2021005488
import random
import time
def bubbleSort(array):
    #função bubble sort, percorre o vetor comparando a casa mais a direita até a casa mais a esquerda achando
    #o menor valor e percorrendo todo o vetor várias vezes
      for i in range(len(array)):

        for j in range(0, len(array) - i - 1):

            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j+1]
                array[j+1] = aux 
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
def quick_sort(array, start, end):
    if start >= end:
        return
    #quicksort vai subdividindo o vetor e organizando por repartições dele até ele estar ordenado, faz uso da recursividade    
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)
array = []#array onde os 5000 valores vão ser inseridos 
while len(array) <5000:#While para gerar 5000 valores aleatórios
    valor = random.randrange(1 , 20000)
    array.append(valor)#coloca o valor no array
array_copia = array #cria uma cópia do Array para usar o mesmo conjunto para medição do tempo
#chamadas das funções do quickSort
print('ordenando array com QuickSort:')
begin = time.time()
quick_sort(array_copia, 0, len(array_copia)-1)
end = time.time()
print('Array ordenado, tempo total:')
print((end - begin))
#chamadas das funções do BubbleSort
print('ordenando array com Bubble Sort:')
inicio = time.time()
bubbleSort(array)
fim = time.time()
print('Array ordenado, tempo total:')
print((fim - inicio)) 
#coloca os tempos em variaveis para comparação de qual foi a melhor
temp_quick = end - begin
temp_bubble = fim - inicio
#mostra qual foi a melhor
if temp_quick < temp_bubble:
    dif = float(temp_quick - temp_bubble)
    print('O QuickSort foi '+ str(dif) + ' ms mais rápido!')
else:
    dif = float(temp_bubble - temp_quick )
    print('O BubbleSort foi '+ str(dif) + ' ms mais rápido!')