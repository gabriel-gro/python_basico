# Estruturas Condicionais - get pedaços de string e testando com if

if __name__ == "__main__":
    vazio = "Vazio"
    cheio = "Cheio"

    num = input()
    primeiroChar = num[:1]
    ultimoChar = num[-1:]
    soma = int(primeiroChar) + int(ultimoChar)
    mult = int(primeiroChar) * int(ultimoChar)
    if(soma == 7 or soma == 8):
        if(mult == 12):
            situacao = vazio
    else:
        situacao = cheio
    print(situacao)