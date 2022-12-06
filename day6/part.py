f = open("input.txt","r")
buf = []
i = f.readline()
for j in range(14,len(i)):
  stri = "".join(set(i[j-14:j]))
  if(len(stri)==14):
    print(j)
    break
