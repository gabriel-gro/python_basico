n=int(input())
matriz=[]
for i in range(n):
  linha=list(map(int,input().split()))
  matriz.append(linha)
somafora=0
somadentro=0
for i in range(n):
  for j in range(n):
    if ((i+j>=n-1) and (i>=j)):
      somadentro+=matriz[i][j]
    else:
      somafora+=matriz[i][j]
  print()
print(somadentro)
print(somafora)
