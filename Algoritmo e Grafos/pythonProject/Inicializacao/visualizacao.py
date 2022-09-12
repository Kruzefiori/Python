'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

visualizacao - Funções para obter plotar imagens de grafos.
Mais informações: https://igraph.org/python/tutorial/latest/tutorial.html#layouts-and-plotting

05/09/2022
===================================================='''

import igraph

'''Visualização do Grafo: Função para obter uma imagem de um grafo da biblioteca iGraph
Entrada: execucao (True/False); grafo (tipo igraph.Graph())
Saída: arquivo .png'''
def visualizarGrafo(execucao, grafo):
    if execucao == True: # True para visualizar a imagem ou False
        grafo.vs[0]
        layout = grafo.layout("fr")  # Layouts: kk, drl, fr, tree
        visual_style = {} # Vetor com as características visuais do grafo
        visual_style["vertex_size"] = 40 # Tamanho do vértice
        visual_style["vertex_shape"] = "circle" # Formatos: triangle, circle, square
        visual_style["vertex_label_size"] = 20 # Tamanho do rótulo do vértice
        visual_style["margin"] = 30 #Margem do grafo em relação a borda da figura.
        grafo.vs["color"] = str('#') + '33FF00' # Cores: Az=99CCFF; Cinz=CCCCCC ; Am=FFFF00; Vd=33FF00; Lar=FFCC00; Ros=FF00FF
        visual_style["autocurve"] = True # Considera arestas curvas. False para arestas retas.
        igraph.plot(grafo, layout=layout, **visual_style)
    return