import numpy as np

f = open("input.txt",'r')
H = [0,0]
T = [0,0]
prev_H = [0,0]

#mat = np.zeros([5,6])
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

for i in f:
  (k,j) = direct(i.strip().split())
  H[k] = H[k]+j
  #print(i)
  #print(H)
  nu = j/abs(j)
#  for l in range(abs(j)):
 #   if(mat[int(H[0]),int(H[1])]!=2):
  #    mat[int(H[0]),int(H[1])] = 1
   # H[k]+=nu
  flag = 0
  #mat[int(H[0]),int(H[1])] = 1
  for l in [-1,0,1]:
    for m in [-1,0,1]:
      if([T[0]+l,T[1]+m]==H):
        flag = 1
        break
    if(flag==1):
      break
  if(not flag):
    while(1):
   #   mat[int(T[0]),int(T[1])] = 2
      visit.append(str([int(T[0]),int(T[1])]))
  #    mat[int(T[0]),int(T[1])] = 2
      T[(k+1)%2]=H[(k+1)%2]
      T[k]+=nu
  #    print(mat)
      visit.append(str([int(T[0]),int(T[1])]))
      if(T[k]==H[k]-nu):
        break
 # mat[int(T[0]),int(T[1])] = 2
  #print(np.flipud(mat))
  #mat = np.zeros([5,6])
  #print("end")
  #print(visit)
print(len(list(set(visit))))
