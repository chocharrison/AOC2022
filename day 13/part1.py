f = open("input.txt",'r')
index = []
lis = []
ind = 1
def check(lis1,lis2):
  #print(lis1,lis2)
  for i in range(len(lis1)):
    try:
      j = lis2[i]
    except:
      return 0
    if(isinstance(lis1[i],int) and isinstance(lis2[i],int)):
      if(lis1[i] < lis2[i]):
        return 1
      elif(lis1[i] > lis2[i]):
        return 0
    elif(isinstance(lis1[i],int) and isinstance(lis2[i],list)):
      j = [lis1[i]]
      j = check(j,lis2[i])
      if(j==-1):
        continue
      return j
    elif(isinstance(lis1[i],list) and isinstance(lis2[i],int)):
      j = [lis2[i]]
      j = check(lis1[i],j)
      if(j==-1):
        continue
      return j
    else:
      j = check(lis1[i],lis2[i])
      if(j==-1):
        continue
      return j
  if(len(lis1) < len(lis2)):
    return 1
  return -1

for i in f:
  if(i=='\n'):
    if(check(lis[0],lis[1])==1):
      index.append(ind)
    ind+=1
    lis = []
  else:
    lis.append(eval(i.strip()))
if(check(lis[0],lis[1])):
  index.append(ind)
print(index)
print(sum(index))
