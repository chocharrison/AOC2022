
f = open("input.txt","r")
sum1 = 0
stri = ''
for i in f:
  if(i == '\n'):
    sum1+=len("".join(set(stri)))
    stri = ''
  stri += i.strip()
sum1+=len("".join(set(stri)))
print(sum1)
