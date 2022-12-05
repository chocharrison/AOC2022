f = open("input.txt","r")
lis = []
for i in f:
  lis.append(int(i.strip()))
flag = 0
for i in range(len(lis)):
  for j in range(i+1,len(lis)):
    for k in range(j+1,len(lis)):
      if(lis[i]+lis[j]+lis[k] == 2020):
        print(lis[i]*lis[j]*lis[k])
        flag = 1
        break
      if(flag):
        break
    if(flag):
      break
