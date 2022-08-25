##
#   Autor: Victor Kruze Fiori
#   Mat: 2021005488
#   Atividade 01 - ID: ATV1
#   Assunto:  Preparação do Ambiente para Atividades
#   Arquivo Principal - Main
##
from functions.write.f_escrita import salva_dado    #import do arquivo que armazena funções de escrita
from functions.read.f_leitura import leitura_matriz #import do arquivo que armazena funções de leitura
import sys #import do módulo sys pra leitura do parametro da main

if __name__ == '__main__':
    path = 'exemplo'                                                             #Seta o nome do arquivo a ser lido como o do exemplo.txt
    if len(sys.argv) > 1:                                           #porém se for recebido algum argumento indicando algum arquivo
        path = sys.argv[1]                                                       #o código utiliza o arquivo recebido como parametro
    res = leitura_matriz(path)                                          #realiza a leitura da matriz chamando a função de leitura
    salva_dado(str(path) + ' ' + str(res[0]) + ' ' + str(res[1]))   #salva os dados no formato nome_instância qtd_linhas qtd_colunas.
