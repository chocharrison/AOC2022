
f = open("input.txt","r")
sum1 = 0
stri = ''
flag = 0
for i in f:
  if(i == '\n'):
    sum1+=len("".join(set(stri)))
    stri = ''
    flag = 0
  elif(flag == 1):
    stri = ''.join(set(stri).intersection(i.strip()))
  else:
    stri = i.strip()
    flag = 1
sum1+=len("".join(set(stri)))
print(sum1)
