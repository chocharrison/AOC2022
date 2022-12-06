f = open("input.txt",'r')
sum = 0
i = f.readline().strip()
for j in range(len(i)):
  if(i[j-1]==i[j]):
    sum+=int(i[j])
print(sum)
