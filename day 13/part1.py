f = open("test",'r')
comp = []

def compare(left,right):
  try:
    y = -1
    for i in range(len(left)):
     # print(left[i],right[i])
      if(type(left[i])==int and type(right[i])==int):
        if(left[i] > right[i]):
          return 0
        elif(left[i] < right[i]):
          return 1
      elif(type(left[i])==list and type(right[i])==int):
        y = compare(left[i],[right[i]])
      elif(type(left[i])==int and type(right[i])==list):
        y = compare([left[i]],right[i])
      else:
        y = compare(left[i],right[i])
      if(y!= -1):
        return y
    if(len(left) < len(right)):
      return 1
  except:
    return 0
  return -1


count = 0
for i in f:
  if(i=='\n'):
    print(comp[0])
    print(comp[1])
    count+=compare(comp[0],comp[1])
    comp = []
  else:
    comp.append(eval(i.strip()))
print(count)
