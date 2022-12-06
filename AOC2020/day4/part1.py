import re
f = open("input.txt","r")
valid = 0
lis = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
opt = "cid"
Dic = dict.fromkeys(lis)
for i in f:
  if(i=='\n'):
    Dic['valid'] = 'no'
    if(all(Dic.values())):
      valid +=1
      Dic['valid'] = 'yes'
    print(Dic)
    Dic = dict.fromkeys(lis)
  else:
    stri = re.split(r'[: ]',i.strip())
    j = 0
    while(j<len(stri)):
        try:
          Dic[stri[j]] = stri[j+1]
        except:
          k = 0
        j+=2
Dic['valid'] = 'no'
if(all(Dic.values())):
  valid +=1
  Dic['valid'] = 'yes'
print(Dic)
print(valid)
