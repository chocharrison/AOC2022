f = open("input.txt",'r')
valis = 0
for i in f:
  lis = i.strip().split()
  lis2 = (" ".join(set(lis))).split()
  if(len(lis)==len(lis2)):
    valis+=1
print(valis)
