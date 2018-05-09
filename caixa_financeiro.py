# Caixa Financeiro imprimindo o menor valor retirado e o maior valor retirado

codigo = int(input())
numero = 0.0
dados = 0
maior = 0
menor = 9999999

while codigo != 0:
    numero = float(input())
    if codigo == 1:
        dados += numero
        if maior < numero:
            maior = numero
    elif codigo == 2:
        dados -= numero
        if menor > numero:
            menor = numero
    codigo=int(input())
    
print(float(dados))

print(float(maior))

if menor == 9999999:
    print(float(0))
else:
    print(float(menor))


