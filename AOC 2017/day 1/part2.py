f = open("input.txt",'r')
sum = 0
i = f.readline().strip()

for j in range(int(len(i)/2)):
  if(i[j]==i[j+int(len(i)/2)]):
    sum+=int(i[j])*2
print(sum)
