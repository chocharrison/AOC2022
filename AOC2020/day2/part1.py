import re
f = open("input.txt","r")
res = 0
for i in f:
  val = i.strip().split()
  rang = val[0].split("-")
  rang = [int(rang[0]),int(rang[1])]
  num = len([m.start() for m in re.finditer(val[1][0], val[2])])
  if(num >= rang[0] and num <= rang[1]):
    res+=1

print(res)
