from classes import Aluno , Grade
#essa maneira prova que as classes estão agregadas já que só trazendo essas duas consigo acessar as outras.

if __name__ == '__main__':

    aluno1 = Aluno('2021000000', 'Victor' , 'Sistemas de informação')
    aluno2 = Aluno ('2021023231' , 'Joaozinho' ,'Ciencia da computação')
    aluno1.setGrade('SIN')
    aluno2.setGrade('CCO')
    grade1 = Grade('Sistemas de informação')
    grade2 = Grade('Ciencia da computação')
    grade1.addMateria('Com112', 'Orientada', 64, False)
    grade1.addMateria('SLA112', 'introdução a prog', 64, True)
    grade1.addMateria('DIS113', 'Economia', 64, True)
    grade1.addMateria('OOP556', 'Introdução a sistemas', 64, True)
    grade1.addMateria('JJX093', 'metodologia', 64, True)
    grade2.addMateria('SLA999', 'robotica', 64, True)
    grade2.addMateria('DIS113', 'Economia', 64, True)
    grade2.addMateria('AAAB', 'aaaaaa', 64, True)
    aluno1.addHistorico('Com112', 'Orientada', 64, False)
    aluno1.addHistorico('SLA999', 'robotica', 64, True)
    aluno1.addHistorico('SLA112', 'introdução a prog', 64, True)
    aluno1.addHistorico('DIS113', 'Economia', 64, True)
    aluno2.addHistorico('SLA999', 'robotica', 64, True)
    aluno2.addHistorico('Com112', 'Orientada', 64, False)
    aluno2.addHistorico('DIS113', 'Economia', 64, False)
    aluno2.addHistorico('AAAB', 'Materia aleatoria', 64, True)
    
    print(aluno1.getName())
    print('Materias realizadas:')
    aluno1.getHist()
    aluno1.getCh()
    print()
    print(aluno2.getName())
    print('Materias realizadas:')
    aluno2.getHist()
    aluno2.getCh()
    

    listaAlunos = [ aluno1 , aluno2]
    for each in listaAlunos:
        if each.getGrade() == 'SIN':
            print('Grade de Sistemas')
            grade1.getCargaHorarioTot()
        elif each.getGrade() == 'CCO':
            print('Grade de CCO')
            grade2.getCargaHorarioTot()


   



