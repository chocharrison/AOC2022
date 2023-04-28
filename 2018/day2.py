f = open("input","r")
two = three = 0
for i in f:
  l = [0]*26
  for j in i.strip():
    l[ord(j)-ord('a')] += 1
  if(2 in l):
    two+=1
  if(3 in l):
    three+=1
print(two*three)
