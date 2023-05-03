f = open("input",'r')
l = 0
k1 = 0
for i in f:
  i = i.strip()
  l1 = len(i)
  j = 0
  k = 0
  while(j < len(i)):
    if(i[j]=='\\' or i[j]=='\"' or i[j]=='\''):
        k+=1
    j+=1
    k+=1
  k1 += l1
  l+=k+2
print(l-k1)
