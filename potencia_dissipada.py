# Cálculo da potência dissipada em um resistor elétrico
# Pode ser realzado a partir da seguinte fórmula:
# Quando a leitura da corrente não está disponível: 
#                   Pot=U²/R   ~ U : Tensão (volts) | R: Resistência (ohms)

# Crie um programa que calcule a potência dissipada a partir de N medições realizadas,
# armazene os resultados em uma lista e por fim mostre a potência média dissipada.

# pDissipada = tensao^2 / resistencia
def potenciaDissipada(u, r):
    return (u * u)/ r

def potMediaDissipada(listPotencias):
    soma = 0
    for p in listPotencias:
        soma = soma + p
    
    # media potencia dissipada
    return soma / len(listPotencias)

def main():
    tamList = int(input())
    listPot = []
    for i in range(tamList):
        u, r = map(float, input().split())
        listPot.append(potenciaDissipada(u, r))

    print(potMediaDissipada(listPot))

main()    