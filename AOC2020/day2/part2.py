import re
f = open("input.txt","r")

res = 0
for i in f:
  [rang,val,stri] = i.strip().split()
  rang = rang.split("-")
  rang = [int(rang[0]),int(rang[1])]
  if((stri[rang[0]-1] == val[0])^(stri[rang[1]-1] == val[0])): 
    res+=1

print(res)
