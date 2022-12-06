
f = open("input.txt","r")
num = []
for i in f:
  startC = startR= 0
  endC = 127
  endR = 7
  for j in i:
    if(j=="F"):
      endC = (startC+endC)//2-1
    elif(j=="B"):
      startC = (startC+endC)//2+1
    elif(j=="L"):
      endR = (startR+endR)//2-1
    elif(j=="R"):
      startR = (startR+endR)//2+1
  num.append(startR+startC*8)
  num.sort()
  missed = sorted(set(range(num[0], num[-1])) - set(num))
print(missed)
