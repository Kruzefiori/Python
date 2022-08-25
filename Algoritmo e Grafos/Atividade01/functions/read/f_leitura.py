##
#   Autor: Victor Kruze Fiori
#   Mat: 2021005488
#   Atividade 01 - ID: ATV1
#   Assunto:  Preparação do Ambiente para Atividades
#   Arquivo dedicado para funções de leitura de arquivos
##

import numpy as np  #import do módulo numpy para trabalhar com matrizes e arrays

def leitura_matriz(dataset):
    caminho_data_set = "Datasets/" + dataset + ".txt"   #setter do path do arquivo recebido como parametro enviado pela main
    matriz = np.loadtxt(caminho_data_set)   #função loadtxt, carrega os dados do arquivo pelo caminho configurado acima
    info = np.shape(matriz) #faz a variável info que recebe a função do numpy "shape" que retorna o formato do array recebido
    return info             #em forma de uma tupla com o tamanho da linha e da coluna.