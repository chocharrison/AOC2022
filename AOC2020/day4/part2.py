import re
f = open("input.txt","r")
test = 2
valid = 0
lis = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
opt = "cid"

ecl = ["amb","blu","brn","gry","grn","hzl","oth"]
def height(hgt):
  if(hgt[-2:] == 'in'):
    if(int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76):
      return 1
    print("height in no")
  elif(hgt[-2:] == 'cm'):
    if(int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193):
      return 1
    print("height cm no")
  return 0

def hair(hcl):
  if(hcl[0] !="#" or len(hcl)!=7):
    print("# no in hair")
    return 0
  try:
    int(hcl[1:],16)
    return 1
  except:
    print("not hex in hair")
    return 0

def validator(Dicti):
    if(not all(Dicti.values())):
      print("no data")
      return 0
    if(int(Dicti["byr"]) <= 1920 or int(Dicti["byr"]) >= 2002):
      print("birth no")
      return 0
    if(int(Dicti["iyr"]) <= 2010 or int(Dicti["iyr"]) >= 2020):
      print("issue no")
      return 0
    if(int(Dicti["eyr"]) <= 2020 or int(Dicti["eyr"]) >= 2030):
      print("expire no")
      return 0
    if(not height(Dicti["hgt"])):
      return 0
    if(not hair(Dicti["hcl"])):
      return 0
    if(Dicti["ecl"] not in ecl):
      print("eye colour not in list")
      return 0
    if(len(Dicti["pid"]) != 9 and not Dicti["pid"].isdigit()):
      print("pid not 9 len")
      return 0
    print(Dicti["byr"])
    return 1

Dic = dict.fromkeys(lis)
for i in f:
  if(i=='\n'):
    valid+=validator(Dic)
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
valid+=validator(Dic)
print(valid)
if(test != valid):
  print("failed")
