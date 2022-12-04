f = open("input.txt","r")
pair = 0

def sublist(ls1, ls2):
    def get_all_in(one, another):
        for element in one:
            if element in another:
                yield element

    for x1, x2 in zip(get_all_in(ls1, ls2), get_all_in(ls2, ls1)):
        if x1 != x2:
            return False

    return True

for i in f:
  lisly = i.strip().split('-')
  lislis = lisly[1].split(',')
  if((int(lisly[0]) - int(lislis[1]))*(int(lislis[0]) - int(lisly[2])) <= 0):
    pair+=1
    print(i)
print(pair) 
