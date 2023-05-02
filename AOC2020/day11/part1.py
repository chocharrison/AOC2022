import copy
f = open("input",'r')
nummy = [0]
for i in f:
  nummy.append(int(i))
nummy.sort()
nummy.append(nummy[-1]+3)
print(nummy)
Dic = {1:0,2:0,3:0}
for i in range(1,len(nummy)):
  Dic[nummy[i]-nummy[i-1]]+=1
print(Dic[1]*Dic[3])
