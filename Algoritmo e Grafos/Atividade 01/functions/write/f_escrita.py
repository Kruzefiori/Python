##
#   Autor: Victor Kruze Fiori
#   Mat: 2021005488
#   Atividade 01 - ID: ATV1
#   Assunto:  Preparação do Ambiente para Atividades
#   Arquivo dedicado para funções de escrita em arquivos
##
def salva_dado(resultado):
    file = open('Datasets_respostas\Respostas.txt' , 'a+') #abre o arquivo que será utilizado para guardar as respostas
    file.writelines(resultado+'\n')                         #escreve no arquivo aberto o resultado obtido pela leitura de matriz e faz uma quebra de linha
    file.close()                                            #fecha a execução do arquivo