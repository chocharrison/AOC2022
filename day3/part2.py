f = open("input.txt","r")
score = 0
flag = 0
strli = []
for i in f:
  flag+=1
  strli.append(i.strip())
  if(flag == 3):
    ch = ''.join(set(strli[0]).intersection(strli[1]).intersection(strli[2]))
    if(ord(ch) >= 97):
      score+= ord(ch)-97+1
    else:
      score+= ord(ch)-65+27
    strli = []
    flag = 0
print(score)
