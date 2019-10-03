# Fazendo calculo de valor relacionando string com valores inteiros

if __name__ == "__main__":
    entrada = str(input())

    va = int(input())
    vb = int(input())
    vc = int(input())
    
    qtdA = 0
    qtdB = 0
    qtdC = 0

    for s in entrada:
        if s == 'a':
            qtdA += 1
        elif s == 'b':
            qtdB += 1
        elif s == 'c':
            qtdC += 1
    
    somaDeValores = qtdA * va + qtdB * vb + qtdC * vc
    print(somaDeValores)