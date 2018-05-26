# Le uma palavra e informa N prefixo ou N sufixo (usuario escolhe) 

def pre(p, qtd):			# p = minha Palavra e qtd = quantas letras vamos retornar
	i = 0	
	pre = ""	
	while qtd > 0:			# IDEIA: vamos percorrer a palavra e pegar as letras desejadas (serão 'qtd' letras)
		pre += p[i]	
		i += 1				# i começa na primeira letra e vai aumentando
		qtd -= 1			# criterio de parada do while
			
	return pre;	
	
def suf(p, qtd):			# p = minha Palavra e qtd = quantas letras vamos retornar
	i = len(p) - 1			# i recebe o tamanho da paalavra ( diminui 1 para pegar a posição dele no vetor )
	suf = ""	
	while qtd > 0:			# IDEIA: vamos percorrer a palavra de tras para frente e pegar as letras desejadas (serão 'qtd' letras)
		suf = p[i] + suf	# pego a letra (p[i]) e somo com a palavra que ja tenho (suf)
		i -= 1
		qtd -= 1
	
	return suf

def main():
	palavra = input()	
	op = input()
	qtd = int(input())
	
	if op == 'S' or op == 's':
		print(suf(palavra, qtd))
	elif op == 'P' or op == 'p':
		print(pre(palavra, qtd))
		
main()
