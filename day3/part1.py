f = open("input.txt","r")
score = 0;
for i in f:
  (str1,str2) = (i.strip()[:(len(i.strip())//2)],i.strip()[(len(i.strip())//2):])
  ch = ''.join(set(str1).intersection(str2))
  if(ord(ch) >= 97):
    score+= ord(ch)-97+1
  else:
    score+= ord(ch)-65+27
print(score)
