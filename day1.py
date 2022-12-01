f = open("input.txt","r")
max = 0
max1,max2 = 0,0
num = 0
for i in f:
  if(i=="\n"):
    if(num > max):
      max2 = max1
      max1 = max
      max = num
    num = 0
  else:
    num+= int(i.strip())
print(max)
print(max1+max2+max)
