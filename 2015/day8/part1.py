f = open("input",'r')
l = 0
l1 = 0
for i in f:
  i = i.strip()
  l1 += len(i)
  i = i[1:-1]
  j = 0
  k = 0
  while(j < len(i)):
    if(i[j]=='\\'):
      if(i[j+1]=='x'):
        j+=3
      else:
        j+=1
    j+=1
    k+=1
  l+=k
print(l1-l)
