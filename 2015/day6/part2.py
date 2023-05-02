import numpy as np
A = np.zeros((1000, 1000))
print(A)
f = open("input",'r')

for i in f:
  i = i.strip().split()
  if(i[0]=='toggle'):
    start = i[1].split(',')
    end = i[3].split(',')
    A[int(start[0]):(int(end[0])+1),int(start[1]):(int(end[1])+1)] += 2
  else:
    start = i[2].split(',')
    end = i[4].split(',')
    if(i[1]=='on'):
      A[int(start[0]):(int(end[0])+1),int(start[1]):(int(end[1])+1)] += 1
    else:
      A[int(start[0]):(int(end[0])+1),int(start[1]):(int(end[1])+1)] -= 1
      for j in range(int(start[1]),(int(end[1])+1)):
        for k in range(int(start[0]),(int(end[0])+1)):
          if(A[k,j] < 0):
            A[k,j] = 0

print(A.sum())
