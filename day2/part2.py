f = open("input.txt","r")
score = 0;
RockDic = {"A":0, "B":1 , "C":2}
ResDic = {"X":0 , "Y":1 , "Z":2}
for i in f:
  val = i.split()
  res = ResDic[val[1]]
  if(res == 0):
    score+= (RockDic[val[0]]-1)%3+1
  elif(res == 1):
    score+= RockDic[val[0]]+3+1
  else:
    score+= (RockDic[val[0]]+1)%3+1+6
print(score)
