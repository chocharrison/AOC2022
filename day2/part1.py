f = open("input.txt","r")
result = 0;
RockDic = {"A":1 , "B":2 , "C":3 ,"X":1 , "Y":2 , "Z":3}
for i in f:
  val = i.split()
  score = RockDic[val[1]] - RockDic[val[0]]
  if(score == 1 or score == -2):
      result+= 6
  elif(score==0):
      result+= 3
  result+=RockDic[val[1]]
print(result)
