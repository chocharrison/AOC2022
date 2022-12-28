import math
f = open("input.txt",'r')
def SnafuToDec(snafu):
  pos = 1
  Dec = 0
  for i in snafu[::-1]:
    if(i=='-'):
      i = -1
    elif(i=='='):
      i = -2
    Dec += int(i)*pos
    pos*=5
  return Dec

def DecToSnafu(dec):
  snifu = ''
  flag = 0
  while(flag != 2):
    q = dec//5
    rem = dec%5
    if(q <= 1):
      flag +=1
    if(rem == 3):
      snifu = '='+ snifu
      q+=1
    elif(rem == 4):
      snifu = '-' + snifu
      q+=1
    else:
      snifu = str(rem) + snifu
    dec = q
  return snifu
sum1 = 0
for i in f:
  num = SnafuToDec(i.strip())
  sum1+=num

print(DecToSnafu(sum1))
