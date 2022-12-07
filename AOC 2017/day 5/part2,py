f = open("input.txt",'r')
lis = []
for i in f:
  lis.append(int(i.strip()))
print(lis)
i = 0
prev = 0
j = 0
while(i < len(lis)):
  prev = i
  i += lis[i]
  if(lis[prev] >= 3):
    lis[prev] -= 1
  else:
    lis[prev] += 1
  j+=1
print(lis)
print(j)
