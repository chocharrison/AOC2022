f = open("input.txt",'r')
sum = 0
for i in f:
  j = i.strip().split()
  j = [int(x) for x in j]
  sum+= max(j)-min(j)
print(sum)
