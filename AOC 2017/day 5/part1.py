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
  lis[prev] += 1
  j+=1
print(j)
