pos = 325489
i = 1
j = 0
while(1):
  if(pos <= i*i):
    break
  i+=2
  j+=1
k = 1
while(1):
  if(i*i - k*(i-1) <= pos):
    break
  k+=1
print(k,i,j,i*i - k*(i-1))
fin = (pos - (i*i - k*(i-1)))
if(fin < j):
  fin = i-1-fin
print(fin)
