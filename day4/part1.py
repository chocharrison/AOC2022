f = open("input.txt","r")
pair = 0

for i in f:
  lisly = i.strip().split('-')
  lislis = lisly[1].split(',')
  if((int(lisly[0]) - int(lislis[1]))*(int(lislis[0]) - int(lisly[2])) <= 0):
    pair+=1
print(pair) 
