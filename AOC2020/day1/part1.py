f = open("input.txt","r")
lis = []
for i in f:
  lis.append(int(i.strip()))
while(lis):
  num =  2020 - lis.pop()
  for j in lis:
    if(j==num):
      print("here")
      print(j*(2020 - num))
      break
