import copy
f = open("input",'r')
g = []

for i in f:
  i = i.split()
  g.append([0,i[0],int(i[1])])
for j in range(len(g)):
  acc = 0
  if(g[j][1]=='acc'):
    continue
  inst = copy.deepcopy(g)
  if(inst[j][1]=='jmp'):
    inst[j][1] = 'nop'
  else:
    inst[j][1] = 'jmp'
  i = 0
  while(i < len(inst) and inst[i][0]!=1):
    inst[i][0] = 1
    if(inst[i][1]=='acc'):
      acc+=inst[i][2]
      i+=1
    elif(inst[i][1]=='jmp'):
      i+=inst[i][2]
    else:
      i+=1
  if(i >= len(inst)):
    print(acc)
