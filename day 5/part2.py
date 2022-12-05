import re
f = open("input.txt","r")
Dic = {}
for i in range(1,10):
  Dic[i] = []
for j in f:
  if (j == "\n"):
    break
  lis = [i for i, ltr in enumerate(j) if ltr == '[']
  for k in lis:
    ind = int(k/4+1)
    Dic[ind] = [j[k+1]] + Dic[ind]
print(Dic)
for i in f:
  lis = i.split()
  num = int(lis[1])
  src = int(lis[3])
  des = int(lis[5])
  Dic[des] = Dic[des] + Dic[src][len(Dic[src]) - num:]
  Dic[src] = Dic[src][:len(Dic[src]) - num]
print(Dic)
stri = ''
for i in Dic:
  stri += Dic[i][-1]
print(stri)
