
def corrigePalavra(l, erro, palavra):			
	return palavra.replace(erro, l)  	# todos lugares que tiver o 'erro' troca por 'l'

# Acredito que o professor possa reclamar na prova de usar esse funcao pronta
# entao coloca um while e cria uma variavel recebendo os valores como abaixo:

#	saida = ""
#	whiel i < (len(palavra) - 1):
#		if palavra[i] != erro:
#			saida += palavra[i]
#		else:
#			saida += l

def main():
	l = str(input())
	erro = str(input())
	qtdPalavras = int(input())

	i = 0
	saida = ""

	while i < qtdPalavras:
		palavra = str(input())
		saida += corrigePalavra(l, erro, palavra) + str('\n') # Chama funçao de correcao e armazena a palavra na variavel "saida" acrescentando uma quebra de linha no fim
		i += 1

	print(saida)	

main()