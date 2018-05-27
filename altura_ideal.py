
def altIdeal(mi, ci, mmi, m, c, mm):			# para futuras conversoes 1M = 1000mm | 1C = 10mm 
	mIdeal = mmi + (ci * 10) + (mi * 1000)		# Transformo a altura ideal passada tudo em milimetros
	minhaAltura = mm + (c * 10) + (m * 1000)
	erro = mIdeal * 0.01				# Nao compreendi a taxa de erro em cima do valor ideal, mas acredito ser isso

	if minhaAltura <= (mIdeal - erro):
		return "sim"
	else:
		return "nao"

def main():
	mi, ci, mmi = map(float, input().split())
	m, c, mm = map(float, input().split())

	print(altIdeal(mi, ci, mmi, m, c, mm))		# chamo a funcao passando os parametros ideais e os meus ja imprimindo o resultado

main()
