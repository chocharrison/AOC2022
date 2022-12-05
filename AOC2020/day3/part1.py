import re
f = open("input.txt","r")

res = 0
length = len(f.readline().strip())
j = 0
for i in f:
  j=(j+3)%length
  if(i[j]=="#"):
    res+=1

print(res)
