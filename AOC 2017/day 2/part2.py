f = open("input.txt",'r')
sum = 0
for i in f:
  j = i.strip().split()
  j = [int(x) for x in j]
  j.sort()
  for k in range(len(j)):
    flag = 0
    for l in range(k+1,len(j)):
      if(j[l]%j[k]==0):
        sum+=j[l]//j[k]
        flag = 1
        break
    if(flag):
      break
print(sum)
