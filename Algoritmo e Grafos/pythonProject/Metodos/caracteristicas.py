'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np


def leitura_matriz(matriz):
    info = np.shape(matriz) #faz a variável info que recebe a função do numpy "shape" que retorna o formato do array recebido
    return info             #em forma de uma tupla com o tamanho da linha e da coluna.

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes

def tipoGrafo(matriz):
    tup_tam = leitura_matriz(matriz)
    for i in range(tup_tam[0]):
        for j in range(tup_tam[1]):
            if matriz[i][i] == 0:
                simples = True
            elif matriz[i][j] == 1 and matriz[j][i] == 0:
                digrafo = True
            elif matriz[i][i] == 1:
                pseudo = True
            else:
                multigrafo = True
    if simples:
        return 0
    if digrafo:
        return 1
    if pseudo:
        return 3
    if multigrafo:
        return 2


def calcDensidade(matriz):
    tup_tam = leitura_matriz(matriz)
    arestas = 0
    if tipoGrafo(matriz) == 0:
        for i in range(tup_tam[0]):
            for j in range(tup_tam[1]):
                arestas += matriz[i][j]
    return 2*arestas/(tup_tam[0]*tup_tam[1]*(tup_tam[1]+tup_tam[0]-1))

def insereAresta(matriz, vi, vj):
    if tipoGrafo == 0:
        matriz[vi][vj] = 1
        matriz[vj][vi] = 1
    else:
        matriz[vi][vj] = 1
    return matriz

def insereVertice(matriz, vi):
    tup_tam = leitura_matriz(matriz)
    tup_tam[0] += vi
    tup_tam[1] += vi
    new_matriz = np.reshape(matriz , tup_tam)
    return new_matriz

def removeAresta(matriz, vi, vj):
    if verificaAdjacencia(matriz , vi , vj):
        matriz[vi][vj] = 0
        return matriz
    else:
        return matriz

def removeVertice(matriz, vi):
    tup_tam = leitura_matriz(matriz)
    tup_tam[0] -= vi
    tup_tam[1] -= vi
    new_matriz = np.reshape(matriz, tup_tam)
    return new_matriz

