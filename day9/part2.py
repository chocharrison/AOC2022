import numpy as np

f = open("test",'r')
He = [0,0]
TT = []
for i in range(9):
  TT.append([0,0])
visit = []

def direct(lis):
  if(lis[0] == 'R'):
    return(1,int(lis[1]))
  if(lis[0] == 'U'):
    return(0,int(lis[1]))
  if(lis[0] == 'L'):
    return(1,-1*int(lis[1]))
  if(lis[0] == 'D'):
    return(0,-1*int(lis[1]))
  return (0,0)

def find(HH,TTT):
  for l in [-1,0,1]:
    for m in [-1,0,1]:
      if([TTT[0]+l,TTT[1]+m]==HH):
        return 1
  return 0


def tailing(H,T,j,k,note=0,num=0):
  nu = j/abs(j)
  flag = 0
  print(H,T,j,k)
  while(1):
    if(find(H,T)):
        return T
    if(note==1):
      visit.append(str([int(T[0]),int(T[1])]))
    T[(k+1)%2]=H[(k+1)%2]
    T[k]+=nu
    if(note==1):
      visit.append(str([int(T[0]),int(T[1])]))

for i in f:
  (kk,jj) = direct(i.strip().split())
  print(i)
  He[kk] = He[kk]+jj
  TT[0] = tailing(He,TT[0],jj,kk)
  for l in range(1,len(TT)-1):
    TT[l] = tailing(TT[l-1],TT[l],jj,kk)
  TT[8] = tailing(TT[7],TT[8],jj,kk,1)
  
print(len(list(set(visit))))
