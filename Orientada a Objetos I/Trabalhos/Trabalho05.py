from classes import horista , diarista , mensalista


if __name__ == "__main__":
    #cadastro de empregados
    empHorista = horista('Margaret Thatcher' , '35 70707070' , 160 , 10)
    empDiariata = diarista('Leonardo da Vinci' , '35 71717171' , 20 , 55)
    empMensalista = mensalista('Amelia Earhart' , '35 72727272' , 1000)
    listaSal = []
    #lista com todos
    listaEmp = [empHorista , empDiariata , empMensalista]
    print('opcoes:')
    for each in listaEmp:
        print ('Nome: {} - Salario: {}'.format(each.getName(), each.getSalario()))
        listaSal.append(each.getSalario())
    
    listaSal.sort() #Coloca a lista de salario de forma ordenada
    for each in listaEmp:#for que acha de quem é o melhor salário
        if each.getSalario() == listaSal[0]:
            choose = each
            break
            
    print('A melhor opcao eh: \n Nome: {} \n Telefone: {} \n Com o salario de: {}'.format(choose.getName() , choose.getTele() , choose.getSalario()));
