import re
f = open("input.txt","r")
test = [2,7,3,4,2]
res = [0,0,0,0,0]
length = len(f.readline().strip())
j = [0,0,0,0]
l = 0
down = 0
for i in f:
  j[0]=(j[0]+1)%length
  j[1]=(j[1]+3)%length
  j[2]=(j[2]+5)%length
  j[3]=(j[3]+7)%length
  for k in range(len(j)):
    if(i[j[k]]=="#"):
      res[k]+=1
  if(down%2 == 0 and down!=0):
    l=(l+1)%length
    if(i[l]=="#"):
      res[4] += 1
  down+=1
resres = 1
print(res)
for i in res:
  resres*=i
print(resres)
if(test != res):
  print("failed")
