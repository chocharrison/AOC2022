import re

rep = 20
f = open("input.txt",'r')
ListMon = []
MonDic = {}
inspect = []
for i in f:
  if(i=='\n'):
    ListMon.append(MonDic)
    MonDic = {}
    inspect.append(0)
  else:
    stri = re.split(', | ', i.strip())
    if(stri[0]=="Starting"):
      MonDic["items"] = []
      for j in stri[2:]:
        MonDic["items"].append(int(j))
    elif(stri[0]=="Operation:"):
      MonDic["operation"] = " ".join(stri[3:])
    elif(stri[0]=="Test:"):
      MonDic["test"] = int(stri[3])
    elif(stri[0]=="If"):
      if(stri[1]=="true:"):
        MonDic["true"] = int(stri[5])
      elif(stri[1]=="false:"):
        MonDic["false"] = int(stri[5])
ListMon.append(MonDic)
inspect.append(0)
for i in range(rep):
  for j in range(len(ListMon)):
    while(ListMon[j]["items"]!=[]):
      inspect[j]+=1
      old = ListMon[j]["items"].pop()
      new = eval(ListMon[j]["operation"])//3
      if(new%ListMon[j]["test"]==0):
        ListMon[ListMon[j]["true"]]["items"].append(new)
      else:
        ListMon[ListMon[j]["false"]]["items"].append(new)

inspect.sort()
print(inspect[-1]*inspect[-2])
