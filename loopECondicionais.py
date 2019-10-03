# Loop com varias condifionais para obter 4 saidas
# Media de notas de uma turma
# Quantos alunos ficaram acima da media
# maior nota
# menor nota

if __name__ == "__main__":
    matricula = input()
    qtdAlunosMais6 = 0
    maiorNota = 0
    menorNota = 99999

    totalNotas = 0
    qtdAlunos = 0
    while matricula != "9999":
        qtdAlunos += 1
        n = 10
        somaNotas = 0
        for i in range(n):
            somaNotas += int(input())
        notaProva = somaNotas / n
        totalNotas += notaProva
        
        if(notaProva < menorNota):
            menorNota = notaProva
        
        if(notaProva > maiorNota):
            maiorNota = notaProva

        if (notaProva >= 6):
            qtdAlunosMais6 += 1
        matricula = input()

    print(totalNotas / qtdAlunos)
    print(qtdAlunosMais6)
    print(maiorNota)
    print(menorNota)