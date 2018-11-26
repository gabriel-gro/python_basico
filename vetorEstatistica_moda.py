# Gerador de estatísticas em relação ao desempenho dos alunos que cursam uma disciplina.
# Para isso, implemente uma função que receba como parâmetro de entrada somente um vetor
# contendo as notas dos alunos em uma prova e retorne o valor da sua moda.

# As notas dos alunos são valores inteiros que variam entre 0 e 10 (incluindo esses valores)

# OBS: Desconsidere o caso em que o conjunto de valores tenha mais de uma moda (haverá sempre apenas uma moda).


# Moda o valor mais frequente de um conjunto de valores
def getModa(listNotas):
    dicNotas = {}
    for item in listNotas:
        if item not in dicNotas:
            dicNotas[item] = 0
        dicNotas[item] = dicNotas[item] + 1

    # pega uma nota qualquer para usar como base para Moda
    moda = listNotas[0]

    for key in dicNotas:
        if dicNotas[moda] < dicNotas[key]:
            moda = key
    return moda

    # iterador para pegar o maximo entre os elementos
    # return max(dicNotas, key=dicNotas.get)


def main():
    # mapeando uma lista como entrada
    vetNotas = list(map(int, input().split()))
    moda = getModa(vetNotas)

    print(moda)

main()    