# Retorna True (verdadeiro) se o numero dor primo e False (falso) se nao for
def ehPrimo(num):
    i = 2
    div = 1
    while i <= num:
        if num % i == 0:        #se for divisivel acrescento 1 nos divisores de num
            div += 1
        i += 1

    if div <= 2:                # é primo se for divisivel por 1 e por ele mesmo
        return True
    else:
        return False

# me retorna quantidade de primos entre N e M
def qtdPrimos(n, m):
    qtd = 0
    i = n
    while i <= m:       # Percorro de n ate m
        if ehPrimo(i):
            qtd += 1
        i += 1
    return qtd

def main():
    n, m = map(int, input().split())
    print(qtdPrimos(n, m))      # chamo a funcao passando os parametros ideais e os meus ja imprimindo o resultado

main()